#!/usr/bin/python3
""" A class that raises an exception
"""


class BaseGeometry:
    """ empty class"""
    def area(self):
        raise Exception('area() is not implemented')
