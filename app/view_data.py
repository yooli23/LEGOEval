from pprint import pprint

from util.data_reader import load_data


if __name__ == '__main__':
    print("Loading...\n")
    task_name = "survey"
    for data_point in load_data(task_name):
        pprint(data_point)
    print("\nDone!")