#!/usr/bin/python3
""" class MyInt which inherits from int:
"""


class MyInt(int):
    """ The class """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other 
