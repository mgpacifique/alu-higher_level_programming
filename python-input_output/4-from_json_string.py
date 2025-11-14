#!/usr/bin/python3
"""Module that defines a from_json_string function"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) from a JSON string

    Args:
        my_str: The JSON string to deserialize

    Returns:
        The Python object represented by the JSON string
    """
    return json.loads(my_str)
