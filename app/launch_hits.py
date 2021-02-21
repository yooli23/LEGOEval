from mturk.api import API
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task_name', required=True)
    args = parser.parse_args()
    api = API()
    api.running_task(args.task_name)