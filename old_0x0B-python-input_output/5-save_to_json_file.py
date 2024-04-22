#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    """
    A program to save a python dict into JSON rep.
    Args:
        my_obj: object to pass
        filename: the name of the file
    Returns:
        rhis function returns the json representation

    """
    with open(filename, 'w', encoding='utf-8') as my_file:
        my_file = json.dump(my_obj, my_file)

my_dict = {
        'id': 12,
        'name': 'toni',
        'place': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
            }
        }

save_to_json_file(my_dict, "my_file.json")

