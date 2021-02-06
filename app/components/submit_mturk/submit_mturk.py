from database import Database
from db_by_josh.query import Query

from util.build_helper import Component


class SubmitMTurk:
    
    @property
    def component(self):
        return Component("SubmitMTurk")

    @classmethod
    def mark_task_complete(cls, state):
        """This function is currently NOT tested"""
        q = Query().select("task_to_hit").where("task_id").equals(state.task_id)
        results = Database.query(q)

        for i in results:
            q = Query().update("mturk").set("complete").equals(1).where("hit_id").equals(i.hit_id)
            Database.query(q)
            
