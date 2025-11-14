#!/usr/bin/python3
"""Module that defines a class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object

    Args:
        obj: An instance of a Class

    Returns:
        A dictionary with all serializable attributes of obj
    """
    return obj.__dict__
