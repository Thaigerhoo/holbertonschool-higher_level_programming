#!/usr/bin/python3
import sys


def print_arguments():
    num_args = len(sys.argv) - 1
    print("Number of argument" + ("s" if num_args != 1 else "") + ":", end=" ")
    print(num_args, end=" ")
    print("argument" + ("s" if num_args != 1 else "") + ":", end="")

    if num_args == 0:
        print(".")
    else:
        print()
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    print_arguments()
