#!/usr/bin/python3
"""

    Module with the function lookup

"""


def lookup(obj):
    """ Function returns a list of all available
        attributes and methods of an object.

    Args:
        obj: instance of the class

    Returns:
        List of attributes

   """

    return dir(obj)
