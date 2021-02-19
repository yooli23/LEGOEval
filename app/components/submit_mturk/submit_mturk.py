from app import db, TaskToHit, MTurk

from util.build_helper import Component


class SubmitMTurk:
    
    @property
    def component(self):
        return Component("SubmitMTurk")

    @classmethod
    def mark_task_complete(cls, state):
        """This function is currently NOT tested"""
        results = TaskToHit.query.filter_by(task_id=state.task_id).all()
        for i in results:
            task = MTurk.filter_by(hit_id=i.hit_id)
            task.complete = True
        db.session.commit()
            
