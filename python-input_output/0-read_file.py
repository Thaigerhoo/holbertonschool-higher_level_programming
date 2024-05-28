#!/usr/bin/python3
""" Module containing a function that reads from a file """


def read_file(filename=""):
    """ Function that reads from a file

    Args:
        filename is passed to the function.

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as file:
        read_data = file.read()
        print(read_data, end='')
