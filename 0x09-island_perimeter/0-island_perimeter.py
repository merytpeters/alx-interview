#!/usr/bin/python3
"""Perimeter of an island represented by 0 and 1 in a matrix
where 1 represents land and 0 represents water"""


def island_perimeter(grid):
    """Returns teh perimeter of the island in a grid"""
    # grid is a list of list
    # Each cell is a square of side length 1
    # Cells are connected horizontally/vertically(not diagonally)
    # grid is rectangular, with its width and height not exceeding 100
    # Only one island or nothing
    # transverse the matrix and check for 1's
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # print(grid[i][j])
            if grid[i][j] == 1:
                # Update perimeter four sides of a square
                perimeter += 4

                """Check for adjancent land cells to avoid
                double-counting shared edges
                Example if the squares are side by side -2"""
                if i > 0 and grid[i - 1][j] == 1:
                    # Land above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    # Land to the left
                    perimeter -= 2
    return perimeter
