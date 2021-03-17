import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import server as config


app = Flask(__name__, static_folder="react_app/build/static", template_folder="react_app/build")
app.config['SECRET_KEY'] = config['server_secret_key']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"] if "DATABASE_URL" in os.environ else 'sqlite:////tmp/test.db'
# DATABASE_URL=$(heroku config:get DATABASE_URL -a your-app) your_process


db = SQLAlchemy(app)


class CustomJSON(db.Model):
    __tablename__ = 'custom_json'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String())        
    count = db.Column(db.Integer())
    json = db.Column(db.String())

    def __init__(self, key, count, json):
        self.key = key
        self.json = json
        self.count = count

    def __repr__(self):
        return f"CustomJSON<{self.id} {self.key} {self.count} {self.json}>"


class TaskToHit(db.Model):
    __tablename__ = 'task_to_hit'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String())
    hit_id = db.Column(db.String())    

    def __init__(self, task_id, hit_id):
        self.task_id = task_id
        self.hit_id = hit_id

    def __repr__(self):
        return f"TaskToHit<{self.id} {self.task_group_id} {self.hit_id} {self.complete}>"


class MTurk(db.Model):
    __tablename__ = 'mturk'

    id = db.Column(db.Integer, primary_key=True)
    task_group_id = db.Column(db.String())
    hit_id = db.Column(db.String())
    complete = db.Column(db.Boolean())

    def __init__(self, task_group_id, hit_id, complete):
        self.task_group_id = task_group_id
        self.hit_id = hit_id
        self.complete = complete

    def __repr__(self):
        return f"MTurk<{self.id} {self.task_group_id} {self.hit_id} {self.complete}>"


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.String())
    state = db.Column(db.String())

    def __init__(self, task_id, state):
        self.task_id = task_id
        self.state = state        

    def __repr__(self):
        return f"Task<{self.id} {self.task_id} {self.state}>"
