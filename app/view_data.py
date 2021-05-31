from pprint import pprint
from collections import Counter
import argparse
import json

from util.data_reader import load_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--task_name', required=True)
    args = parser.parse_args()

    print(f"Loading {args.task_name}\n")    
    
    data = load_data(args.task_name)
    
    for data_point in data:
        try:
            if data_point['complete']:
                print(data_point)
            print('\n---\n')
        except:
            pass        