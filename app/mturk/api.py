import sys
import os
import boto3
import uuid
import json
import time
import signal
import uuid
from threading import Timer

from botocore.exceptions import ClientError
from botocore.exceptions import ProfileNotFound
from db_by_josh.query import Query

import mturk.mturk_utils as mturk_utils
from mturk.settings import mturk as mturk_config
from mturk.settings import environments, worker_requirements
from util.server_util import setup_server, delete_heroku_server

from app import db, TaskToHit, MTurk


THREAD_SHORT_SLEEP = 0.1
HIT_DATA_PATH = "./mturk/hit_data"
SUBMIT_STATUS = 'Submitted'
APPROVE_TIME_LIMIT = 4

class API:



    def __init__(self):
        # Create hits in Sandbox mode
        create_hits_in_live = mturk_config['is_sandbox']

        # Load environment
        self.mturk_environment = environments["sandbox"] if create_hits_in_live else environments["live"]

        # Create session
        mturk_utils.setup_aws_credentials()

        self.hit_data = []
        self.hit_ids = []
        self.task_group_id = None

    def clear_hit_data(self):
        with open(HIT_DATA_PATH, 'w') as file:
            json.dump(self.hit_data, file)

    def create_hit(self, hit_type_id, task_group_id, task_link):
        # Generate random string as the task_id
        task_id = str(uuid.uuid4())
        # Create the HIT
        hit_link, hit_id, response = mturk_utils.create_hit_with_hit_type(
                hit_type_id=hit_type_id,
                task_id=task_id,
                task_link = task_link
            )
        try:
            # link hit_id and hit_type_id
            db.session.add(MTurk(task_group_id, hit_id, complete=False))
            db.session.add(TaskToHit(task_id, hit_id))
            db.session.commit()            
            
            #save hit info locally
            self.hit_data = json.load(open(HIT_DATA_PATH))
            self.hit_ids.append(hit_id)
        except:
            pass

        # The response included several fields that will be helpful later
        hit_info = {}
        hit_info["id"] = response['HIT']['HITId']
        hit_info['type'] = response['HIT']['HITTypeId']
        hit_info['group'] = response['HIT']['HITGroupId']
        hit_info['preview'] = self.mturk_environment['preview'] + "?groupId={}".format(hit_info['group'])
        hit_info['manage'] = self.mturk_environment['manage']
        self.hit_data.append(hit_info)

        with open(HIT_DATA_PATH, 'w') as file:
            json.dump(self.hit_data, file)

        print(hit_info['id'], hit_info['preview'])
    
    def running_task(self, task_name):
        # See if there's enough money in the account to fund the HITs requested
        num_hits = mturk_config['num_hits']
        reward_opt = {
            'type': 'reward',
            'num_total_assignments': num_hits,
            'reward': float(mturk_config['reward']),  # in dollars
        }
        bonus_opt = {
            'type': 'bonus',
            'num_total_assignments': num_hits,
            'bonus': float(mturk_config['bonus']),  # in dollars
        }
        total_cost = mturk_utils.calculate_mturk_cost(payment_opt=reward_opt) + mturk_utils.calculate_mturk_cost(payment_opt=bonus_opt)
        if not mturk_utils.check_mturk_balance(
            balance_needed=total_cost, is_sandbox=mturk_config['is_sandbox']
        ):
            raise SystemExit('Insufficient funds')
        # create hit type
        self.task_group_id = str(int(time.time()))
        qualifications = self.get_qualifications()
        hit_type_id = mturk_utils.create_hit_type(
            hit_title=mturk_config['title'],
            hit_description='{} (ID: {})'.format(
                mturk_config['description'], self.task_group_id
            ),
            hit_keywords=mturk_config['keywords'],
            hit_reward=mturk_config['reward'],
            assignment_duration_in_seconds=mturk_config['assignment_duration'],
            is_sandbox=mturk_config['is_sandbox'],
            qualifications=qualifications,
            auto_approve_delay=mturk_config['auto_approval_delay'],
        )
        # create the task link on heroku
        task_link = setup_server(task_name)
        for hit_idx in range(mturk_config['num_hits']):
            try:
                # Create hit
                self.create_hit(hit_type_id, self.task_group_id, task_link)
            except Exception as error:
                print(error)
        
        # When the task is broken, expire all unassigned hits
        def signal_handler(signal,frame):
            print('Terminate tasks...')
            self.expire_all_unassigned_hits()
            print('Done!')
            sys.exit(0)
 
        signal.signal(signal.SIGINT,signal_handler)
        while True:
            time.sleep(THREAD_SHORT_SLEEP)
    
    def expire_all_unassigned_hits(self):
        """
        Move through the whole hit_id list and attempt to expire the HITs
        """        
        # THIS FUNCTION IS UNTESTED/NOT TESTED, but should work!        
        results = MTurk.query.all()

        for hit in results:
            if hit.complete == 0 and hit.hit_id in self.hit_ids:
                print(hit.hit_id)
                mturk_utils.expire_hit(mturk_config['is_sandbox'], hit.hit_id)

    def approve_work(self, assignment_id, override_rejection=False):
        """
        approve work for a given assignment through the mturk client.
        """
        client = mturk_utils.get_mturk_client(mturk_config['is_sandbox'])
        assignment_status = None
        approve_attempt_num = 0
        if assignment_status != SUBMIT_STATUS and approve_attempt_num < APPROVE_TIME_LIMIT:
            try:
                response = client.get_assignment(AssignmentId=assignment_id)
                if response:
                    assignment_status = response['Assignment']['AssignmentStatus']
            except Exception as error:
                approve_attempt_num += 1                
                timer = Timer(10.0, self.approve_work, [assignment_id, override_rejection])
                timer.start()
                return # start new thread and return this one
        try:
            client.approve_assignment(
                AssignmentId=assignment_id, OverrideRejection=override_rejection
            )
            print('Assignment {} approved.' ''.format(assignment_id))
        except Exception as error:
            print(error)
        client = mturk_utils.get_mturk_client(mturk_config['is_sandbox'])
        
    def worker_complete_task(self, worker_id, assignment_id, hit_id, task_group_id, pay_bonus=False):
        print('User ${} finishes the task, approve the assignment and pay the bonus if bonus > 0'.format(worker_id))

        # Approve work
        self.approve_work(assignment_id)

        # Paying bonus
        if pay_bonus:
            self.pay_worker_bonus(worker_id, assignment_id)

        # Add qualification if is_unique
        unique_qual_name = task_group_id + '_max_submissions'
        if mturk_config['max_assignment'] == 1:
            self.give_worker_qualification(worker_id, unique_qual_name)

    def pay_worker_bonus(self, worker_id, assignment_id):
        """
        Handles paying bonus to a turker.

        Returns True on success and False on failure
        """
        client = mturk_utils.get_mturk_client(mturk_config['is_sandbox'])
        # unique_request_token may be useful for handling future network errors
        unique_request_token = str(uuid.uuid4())
        try:
            client.send_bonus(
            WorkerId=worker_id,
            BonusAmount=str(mturk_config['bonus']),
            AssignmentId=assignment_id,
            Reason='You complete the task successfully, thank you!',
            UniqueRequestToken=unique_request_token,
            )
            print('Paid ${} bonus to WorkerId: {}'.format(mturk_config['bonus'], worker_id))
        except Exception as error:
            print(error)
        return True

    def give_worker_qualification(self, worker_id, qual_name, qual_value=None):
        """
        Give a worker a particular qualification.
        """
        qual_id = mturk_utils.find_or_create_qualification(qual_name, 
                                                        'Worker has done this task',
                                                        mturk_config['is_sandbox'])
        if qual_id is False or qual_id is None:
            print(
                'Could not give worker {} qualification {}, as the '
                'qualification could not be found to exist.'
                ''.format(worker_id, qual_name)
            )
            return
        mturk_utils.give_worker_qualification(
            worker_id, qual_id, qual_value, mturk_config['is_sandbox']
        )
        print('gave {} qualification {}'.format(worker_id, qual_name))
    
    def get_qualifications(self):
        qualifications = worker_requirements

        if mturk_config['max_assignment'] == 1:
            assert self.task_group_id is not None
            unique_qual_name = self.task_group_id + '_max_submissions'
            unique_qual_id = mturk_utils.find_or_create_qualification(
                unique_qual_name,
                'Prevents workers from completing a task too frequently',
                mturk_config['is_sandbox'],
            )
            qualifications.append(
                {
                    'QualificationTypeId': unique_qual_id,
                    'Comparator': 'DoesNotExist',
                    'ActionsGuarded': 'DiscoverPreviewAndAccept',
                }
            )
        return qualifications.copy()
    
    