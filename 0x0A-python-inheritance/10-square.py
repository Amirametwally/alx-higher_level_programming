#!/usr/bin/python3
"""class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square using Rectangle."""

    def __init__(self, size):
        """Intialize a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
