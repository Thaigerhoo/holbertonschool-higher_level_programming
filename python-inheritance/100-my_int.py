#!/usr/bin/python3
"""

Module containing a rebel class.

"""

class MyInt(int):
    def __eq__(self, other):
        """ Method that overrides the == operator to act like != """
        return int(self) != other

    def __ne__(self, other):
         """ Method that overrides the != operator to act like == """
         return int(self) == other
