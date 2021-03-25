from pprint import pprint
from collections import Counter
import json

from util.data_reader import load_data


if __name__ == '__main__':

    task_name = "exp2"
    print(f"Loading {task_name}\n")    
    data = load_data(task_name)
    
    for data_point in data:
        try:
            if data_point['complete']:
                chat = [x['text'] for x in data_point['chat']]
                for row in chat:
                    print(row)
            print('\n---\n')
        except:
            pass        