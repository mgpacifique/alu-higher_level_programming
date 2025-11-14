#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Student class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance

        Args:
            first_name: The student's first name
            last_name: The student's last name
            age: The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance

        Returns:
            A dictionary containing all instance attributes
        """
        return self.__dict__
