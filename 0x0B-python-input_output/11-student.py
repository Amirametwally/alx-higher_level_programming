#!/usr/bin/python3
"""class student"""


class Student:
    """Public instance attributes"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method  that retrieves a dictionary
        representation of a Student instance """

        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            for i in attrs:
                if key == i:
                    new_dictionary[key] = value
        return new_dictionary

    def reload_from_json(self, json):
        """Public method that replaces
        all attributes of the Student instance"""

        for key, value in json.items():
            setattr(self, key, value)
