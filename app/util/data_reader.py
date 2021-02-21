import subprocess
import json

import  sqlalchemy as db


def get_database_url(task_name):
    with open("../appname.json", "r") as f:
        app_name = json.loads(f.read())[task_name]
        print(f"Reading database for {app_name}")
    result = subprocess.check_output(['heroku', 'config:get', 'DATABASE_URL',  '-a',  f'{app_name}'])
    return result.decode('ascii').strip()


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
        del d["pipeline"]
        results.append(d)
    return results