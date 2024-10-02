#!/usr/bin/python3
"""
Function that defines pascal's triangle
Returns a list of lists of integers of n
Returns empty list if n <= 0
"""


def pascal_triangle(n):
    """Pascal"""
    if n <= 0:
        return []

    # Initialise the triangle as an empty list to hold rows
    triangle = []
    for row_index in range(n):
        """Initialize row as list and append 1
        First digit of every row in pascal triangle is 1
        """
        row = []
        row.append(1)

        if row_index > 0:
            # next digits after one
            for i in range(1, row_index):
                # Add values of previous rows left and right
                value = triangle[row_index - 1][i - 1] \
                    + triangle[row_index - 1][i]
                row.append(value)

            row.append(1)
        triangle.append(row)
    return triangle
