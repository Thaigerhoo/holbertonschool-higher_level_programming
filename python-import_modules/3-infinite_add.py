#!/usr/bin/python3
import sys


def add_infinity():

    total = 0
    for arg in sys.argv[1:]:
        total += int(arg)
    print(total)


if __name__ == "__main__":
    add_infinity()
