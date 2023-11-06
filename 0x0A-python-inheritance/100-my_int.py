#!/usr/bin/python3
""" class MyInt that inherits from int"""


class MyInt(int):
    """MyInt is a rebel"""

    def __eq__(self, value):
        """!= operator inverted"""
        return self.real != value

    def __ne__(self, value):
        """== operator inverted"""
        return self.real == value
