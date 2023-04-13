#!/usr/bin/python3
 """the class below inherit from mylist class"""

class MyList(list):


     """this function inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted
        (ascending sort)
        """
        print(sorted(self))
