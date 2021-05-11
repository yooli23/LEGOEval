import os
import sh
import subprocess
import shlex
from flask import render_template, request

from app import app, db
from settings import server as config
from state import State
from main_loop import update as update_fn

@app.before_first_request
def execute_this():
    db.create_all()


@app.route('/')
def index():
    return "Local Test Web App."


@app.route('/<task_id>')
def task(task_id):    
    return render_template('index.html')


@app.route('/<task_id>/init')
def init(task_id):    
    state = State(task_id, flag_server_debug = True)    
    return state.data


@app.route('/<task_id>/update', methods=['POST'])
def update(task_id):
    state = State(task_id, data=request.json, flag_server_debug = True)        
    state = update_fn(state, state.data.get('instruction', ''))
    state.data.pop('instruction', None)
    state.save()    
    return state.data


if __name__ == '__main__':
    parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    react_app_dir = os.path.join(
        parent_dir, 'app', 'react_app'
    )
    os.chdir(react_app_dir)
    # Delete existing generated node modules files
    if os.path.exists(os.path.join(react_app_dir, 'node_modules')):
        sh.rm(shlex.split('-rf ' + 'node_modules'))
    if os.path.exists(os.path.join(react_app_dir, 'build')):
        sh.rm(shlex.split('-rf ' + 'build'))
    packages_installed = subprocess.call(['npm', 'install', react_app_dir])
    if packages_installed != 0:
        raise Exception(
            'please make sure npm is installed, otherwise view'
            ' the above error for more info.'
        )

    webpack_complete = subprocess.call(['npm', 'run', 'build'])
    if webpack_complete != 0:
        raise Exception(
            'Webpack appears to have failed to build your '
            'custom components. See the above for more info.'
        )
    app.run(threaded=True, port=config['port'])