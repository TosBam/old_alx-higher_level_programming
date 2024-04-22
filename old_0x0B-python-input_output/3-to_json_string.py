#!/usr/bin/python3
import json
def to_json_string(my_obj):
    """
    This function return a json representation of an obj
    Args:
        my_obj: object to pass
    Returns:
        returns a json string
    """
    string = json.dumps(my_obj)
    print(string)

my_obj = {
        "name": "Wale",
        "Age": 24,
        "State": [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
            }

        }

to_json_string(my_obj)
