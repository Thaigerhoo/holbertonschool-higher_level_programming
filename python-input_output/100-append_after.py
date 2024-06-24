#!/usr/bin/python3
"""

Module containing a function that inserts text to a file.

"""


def append_after(filename="", search_string="", new_string=""):
    """ Accumulates the modified and adds them back to a file.

    Args:
        filename: The name of the file to modify.
        search_string: The string to search for in each line.
        new_string: The string to insert after lines containing
        `search_string`.

    """
    modified_lines = []

    with open(filename, 'r') as file:
        for line in file:
            modified_lines.append(line)

            if search_string in line:
                modified_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(modified_lines)
