#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """Public instance method"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function validation"""

        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
