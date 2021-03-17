import json
from enum import Enum, auto
import random

from app import db, CustomJSON


class DataLoader:
    """
    Currently, will randomly distribute data to collect.
    Downside is there is no guaruntee the data will actually be collected.
    Future work is to make this system more robust.
    """
    
    def __init__(self, key, count, data):
        """
        key: a unique key associated with your data collection.
        count: the number of times you want each item to be collected.
        data: a list of your json objects (objects must be json serializable).
        """
        self.key = key
        self.count = count
        self.data = data
        self.create_data_if_non_exists()

    def create_data_if_non_exists(self):
        """
        Adds objects to the database if non-exist.
        """
        results = CustomJSON.query.filter_by(key=self.key).all()
        if results != []: return
        for i in self.data:
            db.session.add(CustomJSON(key=self.key, count=self.count, json=json.dumps(i)))
        db.session.commit()

    def pop(self):
        """
        Pops an element that needs work and returns it.
        We decrement the count of an object.
        If no objects left, i.e, all have a count of zero,
        we return a random choice and collect extra data.
        """
        possible_results = CustomJSON.query.filter_by(key=self.key).filter(CustomJSON.count > 0).all()
        if not possible_results:
            possible_results = CustomJSON.query.filter_by(key=self.key).all()
        obj = random.choice(possible_results)
        obj.count -= 1
        db.session.commit()
        return json.loads(obj.json)

