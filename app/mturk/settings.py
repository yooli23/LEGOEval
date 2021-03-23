"""
A file containing all the settings for configuring your task.
"""


# Database options
database = {
    'database_path': "./database/data.db"
}

# Server options
server = {
    'server_secret_key': 'secret',   
    'port': 1234,
    'debug': False,
    'logger': False,
    'front_end_socketio_path': '/visualchatsocket',    
    'server_socketio_path': '/visualchatsocket',
}

# Task options
task = {
    'human_speaks_first': False,    
    'task_name': 'Evaluation Task',  
    'task_short_description': 'You will chat with a bot',
    'task_key_words': "label text, binary, yes, no, context, bonus, grammer, english",       
    'task_instructions': """
                    For this task, you will be chatting with another user.

                    Please complete the pre-task survey, then chat with the other user for approximately 5 minutes.

                    Finally, you will complete a post-task survey.
                    """,    
    'move_instructions_to_top': True,
    'enable_agent_title': True,    
    'prefix_message': True,
    'show_page_number': True,
}

mturk = {
    # If this is False, real money will be deducted
    'is_sandbox': True,
    # basic reward for each HIT
    'reward': '0.50',
    # bonus will be paid if the worker finish the HIT
    'bonus': '0.00',
    # task title
    'title': task['task_name'],
    # Keywords of our hits
    'keywords': task['task_key_words'],
    # Description of the hit
    'description': task['task_short_description'],
    # number of hits
    'num_hits': 3,
    # auto_approval_delay in seconds
    'auto_approval_delay': 60*60*24, # one day
    # max assignment 1- unique worker, 0 - unlimited hits per worker TODO: only works for unique worker now.
    'max_assignment': 1,
    # life time in seconds
    'life_time': 7200, # 2 hours
    # assignment duration in seconds
    'assignment_duration': 1800, # 30 minutes
    # maximum users at a same time
    'maximum_user': 2,
    # embedded page url
    'page_url': 'https://localhost:1234',
    # frame height
    'frame_height': 0, # set to zero for automatic size...
}

# live and sandbox environments
environments = {
    "live": {
        "endpoint": "https://mturk-requester.us-east-1.amazonaws.com",
        "preview": "https://www.mturk.com/mturk/preview",
        "manage": "https://requester.mturk.com/mturk/manageHITs",
        "reward": mturk['reward']
    },
    "sandbox": {
        "endpoint": "https://mturk-requester-sandbox.us-east-1.amazonaws.com",
        "preview": "https://workersandbox.mturk.com/mturk/preview",
        "manage": "https://requestersandbox.mturk.com/mturk/manageHITs",
        "reward": mturk['reward']
    },
}

# qualification
# Please refer to:
# https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
worker_requirements = [
    {
        'QualificationTypeId': "000000000000000000L0", 
        # PercentAssignmentsApproved
        'Comparator': 'GreaterThan',
        'IntegerValues':[98]
    },
]