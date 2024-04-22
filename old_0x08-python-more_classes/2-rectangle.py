#!/usr/bin/python3

""" An empty class object defining a rectangle
"""

class Rectangle:

    """empty class object"""

    def __init__(self, width=0, height=0):
        """ Instantiation with  width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width
        """
        return self.__width

    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)


