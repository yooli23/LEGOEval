#!/usr/bin/env python3

import getpass
import glob
import hashlib
import netrc
import os
import platform
import sh
import shlex
import shutil
import subprocess
import time
import json

region_name = 'us-east-1'
user_name = getpass.getuser()

parent_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
server_source_directory_name = 'react_app'
heroku_server_directory_name = 'heroku_server'

server_process = None

heroku_url = 'https://cli-assets.heroku.com/heroku-cli/channels/stable/heroku-cli'

def setup_heroku_server(
    task_name,
    tmp_dir=parent_dir,
):

    print("Heroku: Collecting files... for ", tmp_dir)
    # Install Heroku CLI
    os_name = None
    bit_architecture = None

    # Get the platform we are working on
    platform_info = platform.platform()
    print("ALERT!")
    print(platform_info) # macOS-11.2.1-x86_64-i386-64bit
    print("\n\n\n")

    if 'Darwin' in platform_info or 'macOS' in platform_info:  # Mac OS X
        os_name = 'darwin'
    elif 'Linux' in platform_info:  # Linux
        os_name = 'linux'
    else:
        os_name = 'windows'

    # Find our architecture
    bit_architecture_info = platform.architecture()[0]
    if '64bit' in bit_architecture_info:
        bit_architecture = 'x64'
    else:
        bit_architecture = 'x86'

    # Remove existing heroku client files
    existing_heroku_directory_names = glob.glob(os.path.join(tmp_dir, 'heroku-cli-*'))
    if len(existing_heroku_directory_names) == 0:
        if os.path.exists(os.path.join(tmp_dir, 'heroku.tar.gz')):
            os.remove(os.path.join(tmp_dir, 'heroku.tar.gz'))

        # Get the heroku client and unzip
        os.chdir(tmp_dir)
        sh.wget(
            shlex.split(
                '{}-{}-{}.tar.gz -O heroku.tar.gz'.format(
                    heroku_url, os_name, bit_architecture
                )
            )
        )
        sh.tar(shlex.split('-xvzf heroku.tar.gz'))

    heroku_directory_name = glob.glob(os.path.join(tmp_dir, 'heroku-cli-*'))[0]
    heroku_directory_path = os.path.join(tmp_dir, heroku_directory_name)
    heroku_executable_path = os.path.join(heroku_directory_path, 'bin', 'heroku')

    server_source_directory_path = os.path.join(
        parent_dir, 'app'
    )
    heroku_server_development_path = os.path.join(
        tmp_dir, '{}_{}'.format(heroku_server_directory_name, task_name)
    )

    # Delete old server files
    sh.rm(shlex.split('-rf ' + heroku_server_development_path))

    # Delete existing generated node modules files
    if os.path.exists(os.path.join(server_source_directory_path, 'react_app', 'node_modules')):
        sh.rm(shlex.split('-rf ' + os.path.join(server_source_directory_path, 'react_app', 'node_modules')))
    if os.path.exists(os.path.join(server_source_directory_path, 'react_app', 'build')):
        sh.rm(shlex.split('-rf ' + os.path.join(server_source_directory_path, 'react_app', 'build')))

    # Copy over a clean copy into the server directory
    shutil.copytree(server_source_directory_path, heroku_server_development_path)

    # Check to see if we need to build
    react_app_dir = os.path.join(heroku_server_development_path, 'react_app')
    # Build the directory, then pull the custom component out.
    print('Build: Detected package.json, prepping build')

    os.chdir(react_app_dir)
    packages_installed = subprocess.call(['npm', 'install', react_app_dir])
    if packages_installed != 0:
        raise Exception(
            'please make sure npm is installed, otherwise view'
            ' the above error for more info.'
        )
    os.chdir(react_app_dir)

    webpack_complete = subprocess.call(['npm', 'run', 'build'])
    if webpack_complete != 0:
        raise Exception(
            'Webpack appears to have failed to build your '
            'custom components. See the above for more info.'
        )

    print("Heroku: Starting server...")

    heroku_server_directory_path = heroku_server_development_path
    os.chdir(heroku_server_directory_path)
    sh.rm(shlex.split('-rf .git'))
    sh.git('init')

    # get heroku credentials
    heroku_user_identifier = None
    while not heroku_user_identifier:
        try:
            subprocess.check_output(shlex.split(heroku_executable_path + ' auth:token'))
            heroku_user_identifier = netrc.netrc(
                os.path.join(os.path.expanduser("~"), '.netrc')
            ).hosts['api.heroku.com'][0]
        except subprocess.CalledProcessError:
            raise SystemExit(
                'A free Heroku account is required for launching MTurk tasks. '
                'Please register at https://signup.heroku.com/ and run `{} '
                'login` at the terminal to login to Heroku, and then run this '
                'program again.'.format(heroku_executable_path)
            )

    heroku_app_name = (
        '{}-{}-{}'.format(
            user_name,
            task_name,
            hashlib.md5(heroku_user_identifier.encode('utf-8')).hexdigest(),
        )
    )[:30]

    while heroku_app_name[-1] == '-':
        heroku_app_name = heroku_app_name[:-1]
    
    # Save the task name and app name to retrieve data in the future
    os.chdir(parent_dir)
    app_names = {}
    if os.path.exists('appname.json'):
        f = open('appname.json', 'r')
        content = f.read()
        app_names = json.loads(content)
        f.close()

    os.chdir(heroku_server_directory_path)
    # Create or attach to the server
    bool_new_app = True
    try:
        subprocess.check_output(
            shlex.split(
                '{} create {}'.format(heroku_executable_path, heroku_app_name)
            )
        )
    except Exception as error:
        # if the app has been created
        print("This app exists, trying to push new changes...")
        bool_new_app = False
        if task_name in app_names:
            pass
        else:
            sh.rm(shlex.split('-rf {}'.format(heroku_server_directory_path)))
            raise SystemExit(
                'You have hit your limit on concurrent apps with heroku, which are'
                ' required to run multiple concurrent tasks.\nPlease wait for some'
                ' of your existing tasks to complete. If you have no tasks '
                'running, login to heroku and delete some of the running apps or '
                'verify your account to allow more concurrent apps'
            )
    try:
        subprocess.check_output(
            shlex.split(
                '{} git:remote -a {}'.format(heroku_executable_path, heroku_app_name)
            )
        )
    except subprocess.CalledProcessError:
        raise SystemExit(
                'Setting git remote error! Please check the appname.json file under git root path and '
                'make sure all the apps are running in your heroku account.'
            )

    # if this task is not in the app list, add it to the app names json file.
    if task_name not in app_names or (task_name in app_names and app_names[task_name] != heroku_app_name):
        app_names[task_name] = heroku_app_name
        b = json.dumps(app_names)
        os.chdir(parent_dir)
        f2 = open('appname.json', 'w')
        f2.write(b)
        f2.close()
    
    os.chdir(heroku_server_directory_path)
    # Enable WebSockets
    try:
        subprocess.check_output(
            shlex.split(
                '{} features:enable http-session-affinity'.format(
                    heroku_executable_path
                )
            )
        )
    except subprocess.CalledProcessError:  # Already enabled WebSockets
        pass

    # commit and push to the heroku server
    os.chdir(heroku_server_directory_path)
    sh.git(shlex.split('add -A'))
    sh.git(shlex.split('commit -m "app"'))
    sh.git(shlex.split('push -f heroku master'))

    subprocess.check_output(
        shlex.split('{} ps:scale web=1'.format(heroku_executable_path))
    )

    os.chdir(parent_dir)

    # Clean up heroku files
    if os.path.exists(os.path.join(tmp_dir, 'heroku.tar.gz')):
        os.remove(os.path.join(tmp_dir, 'heroku.tar.gz'))

    sh.rm(shlex.split('-rf {}'.format(heroku_server_development_path)))

    # create the postgresql add on if creating a new app
    if bool_new_app:
        try:
            print("Creating the heroku postgresql addon...")
            subprocess.check_output(
                shlex.split('{} addons:create heroku-postgresql:hobby-dev --version=10 --app {}'.format(heroku_executable_path, heroku_app_name))
            )
            
        except subprocess.CalledProcessError:
            print("Fail to create the heroku postgresql addon")
            pass

    return 'https://{}.herokuapp.com'.format(heroku_app_name)


def delete_heroku_server(task_name, tmp_dir=parent_dir):
    heroku_directory_name = glob.glob(os.path.join(tmp_dir, 'heroku-cli-*'))[0]
    heroku_directory_path = os.path.join(tmp_dir, heroku_directory_name)
    heroku_executable_path = os.path.join(heroku_directory_path, 'bin', 'heroku')

    heroku_user_identifier = netrc.netrc(
        os.path.join(os.path.expanduser("~"), '.netrc')
    ).hosts['api.heroku.com'][0]

    heroku_app_name = (
        '{}-{}-{}'.format(
            user_name,
            task_name,
            hashlib.md5(heroku_user_identifier.encode('utf-8')).hexdigest(),
        )
    )[:30]
    while heroku_app_name[-1] == '-':
        heroku_app_name = heroku_app_name[:-1]
    print("Heroku: Deleting server: {}".format(heroku_app_name))
    subprocess.check_output(
        shlex.split(
            '{} destroy {} --confirm {}'.format(
                heroku_executable_path, heroku_app_name, heroku_app_name
            )
        )
    )


def setup_server(task_name, tmp_dir=parent_dir):
    return setup_heroku_server(task_name, tmp_dir=tmp_dir)
