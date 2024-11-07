#!/usr/bin/env python3
"""N queens backtracking"""
import sys


def print_usage_and_exit(message, exit_code):
    """Prints a message and exits with the specified exit code."""
    print(message)
    sys.exit(exit_code)


def is_valid(board, row, col):
    """Checks if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if (
            board[i] == col or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(n, row=0, board=None):
    """Recursive backtracking to find all solutions to the N queens problem."""
    if board is None:
        board = []
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if is_valid(board, row, col):
            solve_nqueens(n, row + 1, board + [col])


def main():
    """Main function to validate input and solve the N queens puzzle."""
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N", 1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number", 1)
    if n < 4:
        print_usage_and_exit("N must be at least 4", 1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
