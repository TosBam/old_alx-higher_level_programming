#!/usr/bin/python3
import json

def from_json_string(my_str):
    """

    """
    string = json.loads(my_str)
    print(string)

my_str = '{"name": "Wale", "Age": 24, "State": ["San Francisco", "Tokyo"], "is_active": True, "info": {"age": 36, "average": 3.14}}'

from_json_string(my_str)
