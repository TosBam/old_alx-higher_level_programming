#!/usr/bin/python3
"""Module check class and subclass"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class if not return False
    """
    return isinstance(obj, a_class)
