#!/usr/bin/python3
"""Module that defines a read_file function"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        filename: The name of the file to read (default: "")
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
