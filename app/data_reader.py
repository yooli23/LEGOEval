# import subprocess

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# from settings import server as config


# def get_database_url():
#     app_name = "test"
#     result = subprocess.check_output(['heroku', 'config:get', 'DATABASE_URL',  '-a',  f'{app_name}'])
#     return result


# app = Flask(__name__, static_folder="react_app/build/static", template_folder="react_app/build")
# app.config['SECRET_KEY'] = config['server_secret_key']
# app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()


# db = SQLAlchemy(app)


# class TaskToHit(db.Model):
#     __tablename__ = 'task_to_hit'

#     id = db.Column(db.Integer, primary_key=True)
#     task_id = db.Column(db.String())
#     hit_id = db.Column(db.String())    

#     def __init__(self, task_id, hit_id):
#         self.task_id = task_id
#         self.hit_id = hit_id

#     def __repr__(self):
#         return f"TaskToHit<{self.id} {self.task_group_id} {self.hit_id} {self.complete}>"


# class MTurk(db.Model):
#     __tablename__ = 'mturk'

#     id = db.Column(db.Integer, primary_key=True)
#     task_group_id = db.Column(db.String())
#     hit_id = db.Column(db.String())
#     complete = db.Column(db.Boolean())

#     def __init__(self, task_group_id, hit_id, complete):
#         self.task_group_id = task_group_id
#         self.hit_id = hit_id
#         self.complete = complete

#     def __repr__(self):
#         return f"MTurk<{self.id} {self.task_group_id} {self.hit_id} {self.complete}>"


# class Task(db.Model):
#     __tablename__ = 'task'

#     id = db.Column(db.Integer, primary_key=True)
#     task_id = db.Column(db.String())
#     state = db.Column(db.String())

#     def __init__(self, task_id, state):
#         self.task_id = task_id
#         self.state = state        

#     def __repr__(self):
#         return f"Task<{self.id} {self.task_id} {self.state}>"
