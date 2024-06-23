#!/usr/bin/python3
"""

Module containing a coding challenge.

"""


def pascal_triangle(n):
    # If n is less than or equal to 0, return an empty list.
    if n <= 0:
        return []
    # Initialize the triangle with the first row.
    triangle = [[1]]

    # Generate each row of the triangle.
    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)

        triangle.append(row)

    return triangle
