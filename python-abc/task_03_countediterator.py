#!/usr/bin/python3
"""

Module containig a class that extends the built-in iterator obtained
from the iter function.

"""


class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.count = 0
        self.iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")

    def get_count(self):
        return self.count
