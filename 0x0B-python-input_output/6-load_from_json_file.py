#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    """
    with open(filename, encoding='utf-8') as my_file:
        my_data = json.loads(my_file)
        print(my_data)

load_from_json_file(my_file)
