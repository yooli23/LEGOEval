from pprint import pprint

from util.data_reader import load_data


if __name__ == '__main__':
    print("Loading...\n")
    for data_point in load_data():
        pprint(data_point)
    print("\nDone!")