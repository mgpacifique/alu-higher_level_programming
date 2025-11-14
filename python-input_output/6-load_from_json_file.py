#!/usr/bin/python3
"""Module that defines a load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename: The name of the JSON file to load

    Returns:
        The Python object from the JSON file
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
