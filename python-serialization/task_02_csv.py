#!/usr/bin/python3
import csv
import json
"""

Module containing function that converts data from one format to another.

"""


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write it to data.json.

    Parameters:
        csv_filename: It's the file's name.

    Returns:
        True if the conversion was successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            data = [row for row in csv_reader]

        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
