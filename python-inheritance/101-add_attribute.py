#!/usr/bin/python3
"""

Module containing a function that adds an attribute to an object if possible.

"""


def add_attribute(obj, att, value):
    """ Add an attribute to object  if possible

    Args:
        obj (any): The object to add the attribute to.
        att (str): The name of the attribute being added.
        value (any): The value of the attribute.
    Raises:
        TypeError:If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
