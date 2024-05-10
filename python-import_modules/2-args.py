#!/usr/bin/python3
import sys


def print_arguments():
    num_args = len(sys.argv) - 1

    if num_args == 0:
        print("0 arguments.")
    else:
        arg_args = 'argument' if num_args == 1 else 'arguments'
        print(f"{num_args} {arg_args}:")

    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    print_arguments()
