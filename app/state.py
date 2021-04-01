import json
import time

from app import db, Task
from build import pipeline
from util.build_helper import PipelineHelper, Component, Compute
from build import compute


class State:
    
    def __init__(self, task_id, data=None):
        self.task_id = task_id
        self._load_from_db()
        self._calculate_component_if_needed()
        if data:
            self.data = data

    def _load_from_db(self):        
        """Loads the state data from the database."""        
        result = Task.query.filter_by(task_id=self.task_id).first()
        if not result:     
            task = Task(
                task_id=self.task_id,
                state=json.dumps({'task_id':self.task_id, 'pipeline':PipelineHelper.encode(pipeline)})
            )
            db.session.add(task)
            db.session.commit()
            self._load_from_db()
        else:            
            self.data = json.loads(result.state)

    def _calculate_component_if_needed(self):
        """Calcuates the 'component' key in the state if its None."""

        encoded_pipeline = self.data['pipeline']

        if not encoded_pipeline:
            raise RuntimeError("Pipeline is empty! Expected non-empty pipeline!")

        decoded_pipeline = PipelineHelper.decode(encoded_pipeline)

        first = decoded_pipeline[0]

        # If its a component, its easy
        if isinstance(first, Component):
            self.save()
            return

        # If its a compute object, we need to "compute" the list and then try again
        if isinstance(first, Compute):
            extended_data = compute[first.name](self.data) # passes in dictionary, not State class
            decoded_pipeline = extended_data + decoded_pipeline[1:]
            final_pipeline = PipelineHelper.encode(decoded_pipeline)
            self.data['pipeline'] = final_pipeline
            self._calculate_component_if_needed()
            return
        
        raise RuntimeError("Unknown pipeline object: ", first)

    def save(self):
        """Saves the state to the database."""
        task = Task.query.filter_by(task_id=self.task_id).first()
        task.state = json.dumps(self.data)
        db.session.commit()

    def advance(self):
        """Advances to the next component."""                    
        if len(self.data['pipeline']) > 1:
            self.data['pipeline'].pop(0)
            self._calculate_component_if_needed()
        else:            
            raise Warning("Trying to pop last component!")