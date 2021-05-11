from pprint import pprint
from collections import Counter
import json

from util.data_reader import load_data


if __name__ == '__main__':

    task_name = "my-task-name"

    print(f"Loading {task_name}\n")    
    
    data = load_data(task_name)
        
    for data_point in data:      
        if data_point['complete']:
            pass
      