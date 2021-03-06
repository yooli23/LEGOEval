from flask import render_template, request

from app import app, db
from settings import server as config
from state import State
from main_loop import update as update_fn
from components.submit_mturk.submit_mturk import SubmitMTurk

import sys


@app.before_first_request
def execute_this():
    db.create_all()


@app.route('/')
def index():
    return "I dream of being a web app."


@app.route('/<task_id>')
def task(task_id):    
    return render_template('index.html')


@app.route('/<task_id>/init')
def init(task_id):    
    state = State(task_id, flag_server_debug = False)    
    return state.data


@app.route('/<task_id>/update', methods=['POST'])
def update(task_id):
    state = State(task_id, data=request.json, flag_server_debug = False)   
    instruction = state.data.get('instruction', 'error')    
    state = update_fn(state, instruction)
    if instruction == 'advance': state.advance()        
    if instruction == 'mark_complete': SubmitMTurk.mark_task_complete(state)    
    state.data.pop('instruction', None)
    state.save()    
    return state.data


if __name__ == '__main__':
    app.run(threaded=True, port=config['port'])