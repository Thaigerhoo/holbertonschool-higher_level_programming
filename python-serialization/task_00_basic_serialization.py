#!/usr/bin/python3
import json
"""

Module containing functions that serialize a Python dictionary
to a JSON file and deserializes the JSON file
to recreate the Python dictionary.

"""


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given dictionary and save it to the specified JSON file.

    Parameters:
        data: A Python dictionary.
        filename: It's the file's name.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified JSON file.

    Parameters:
        filename: It's the file's name.

    Returns:
        Deserialized data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
