#!/usr/bin/python3
"""

Module containing different classes using an abstarct method.

"""


from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return 'Bark'


class Cat(Animal):
    def sound(self):
        return 'Meow'
