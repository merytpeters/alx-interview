#!/usr/bin/python3
"""Rotate 2D Matrix
n x n 2D matrix, array of array, not empty
edited-in-place, no copy
rotate 90 degrees clockwise
returns nothing
"""


def rotate_2d_matrix(matrix):
    """Rotate 90 degrees clockwise, to move clockwise
    first row becomes last column, second row second column
    etc"""
    # number of rows
    n = len(matrix)
    for i in range(n):
        # transpose matrix
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
