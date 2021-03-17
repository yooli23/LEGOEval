import subprocess
import json

import  sqlalchemy as db


def get_database_url(task_name):
    try:
        with open("../appname.json", "r") as f:
            loaded_dict = json.loads(f.read())
            if task_name not in loaded_dict:
                raise RuntimeError("Uh oh. This task name does not exist!")
            app_name = loaded_dict[task_name]
            print(f"Reading database for {app_name}")
        result = subprocess.check_output(['heroku', 'config:get', 'DATABASE_URL',  '-a',  f'{app_name}'])
        return result.decode('ascii').strip()
    except:
        raise RuntimeError('"appname.json" in ../app does not exist! Please run the task first via launch_hits.py!')


def query_raw_data(task_name):
    engine = db.create_engine(get_database_url(task_name), echo=False)
    connection = engine.connect()
    metadata = db.MetaData()
    tasks = db.Table('task', metadata, autoload=True, autoload_with=engine)
    query = db.select([tasks])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    return ResultSet


def load_data(task_name):
    results = []
    raw_data = query_raw_data(task_name)
    for i in raw_data:
        d = json.loads(i[2])
        
        for key in ['messages', 'text', 'compare_bot_a', 'compare_bot_b', 'compare_bot_preference', 'pipeline']:
            try:
                del d[key]
            except:
                pass

        results.append(d)
    return results