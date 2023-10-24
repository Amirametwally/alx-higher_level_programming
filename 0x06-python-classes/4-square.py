#!/usr/bin/python3
"""square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """Initialize the Square instance with optional size."""
        self.__size = size

    @property
    def size(self):
        """function that return size"""
        return self.__size

    @size.setter
    def size(self, value):
        """function that set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """function return area"""
        return self.__size ** 2
