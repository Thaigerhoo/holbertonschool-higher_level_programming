#!/usr/bin/python3
"""
Module containing function that returns the
number of lines of a text file.

"""


def number_of_lines(filename=""):
    """ Function that reads from a file and prints its number of lines

    Args:
        Filenameis the file's name.

    Raises
        Exception: when the file can be opened.

    """
    num_lines = 0
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            num_lines += 1
    return num_lines
