from database import Database
import os

from flask import Flask, request, send_from_directory, render_template, jsonify

from settings import server as config
from state import State
from main_loop import update as update_fn


app = Flask(__name__, static_folder="react_app/build/static", template_folder="react_app/build")
app.config['SECRET_KEY'] = config['server_secret_key']


@app.route('/')
def index():
    return "I dream of being a web app."


@app.route('/<task_id>')
def task(task_id):    
    return render_template('index.html')


@app.route('/<task_id>/init')
def init(task_id):    
    state = State(task_id)    
    return state.data


@app.route('/<task_id>/update', methods=['POST'])
def update(task_id):
    state = State(task_id, data=request.json)        
    state = update_fn(state, state.data.get('instruction', ''))
    state.data.pop('instruction', None)
    state.save()    
    return state.data


if __name__ == '__main__':
    app.run(port=config['port'], debug=config['debug'])