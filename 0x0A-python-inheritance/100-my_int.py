#!/usr/bin/python3
""" class MyInt that inherits from int"""


class MyInt(int):
    """MyInt is a rebel"""

    def ___eq__(self, value):
        """!= operator inverted"""
        return self.real != value

    def ___ne__(self, value):
        """== operator inverted"""
        return self.real == value
