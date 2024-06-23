#!/usr/bin/python3
"""

Module containing MixIns that add functionality
to classes in a modular fashion.

"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")


draco = Dragon()
draco.swim()
draco.fly()
draco.roar()
