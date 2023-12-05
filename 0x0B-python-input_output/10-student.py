#!/usr/bin/python3
""" class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """define a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary model of the Student"""
        if (type(attrs) == list and
                all(type(stud) == str for stud in attrs)):
            return {X: getattr(self, X) for X in attrs if hasattr(self, X)}
        return self.__dict__
