#!/usr/bin/python3
"""

Module containing a rebel class.

"""


class MyInt(int):
    def __eq__(self, value):
        """ Method that overrides the == operator to act like != """
        return self.real != value

    def __ne__(self, value):
        """ Method that overrides the != operator to act like == """
        return self.real == value
