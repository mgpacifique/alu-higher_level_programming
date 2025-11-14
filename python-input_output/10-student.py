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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs: A list of attribute names to retrieve (default: None)

        Returns:
            A dictionary containing specified or all instance attributes
        """
        if attrs is None:
            return self.__dict__
        
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
