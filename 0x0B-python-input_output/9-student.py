#!/usr/bin/python3

"""MODULE HAS ONE CLASS STUDENT WITH ONE PUBLIC METHOD"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """__init__ the constructor of the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ghurnnegh obj athnnar amakken json"""
        return self.__dict__
