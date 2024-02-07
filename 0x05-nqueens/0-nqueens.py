#!/usr/bin/python3
"""N queens challenge"""

import sys


def print_solution(queens):
    """Prints the solution in the format [[row1, col1],..., [rowN, colN]]."""
    for row, col in queens:
        print("[{}, {}]".format(row, col), end=" ")
    print()


def is_safe(queens, row, col):
    """Checks if it's safe to place a queen at the given row and column."""
    for r, c in queens:
        # Check if there's a queen in the same column or diagonally.
        if col == c or abs(row - r) == abs(col - c):
            return False
    return True


def solve_nqueens(queens, row, N, solutions):
    """Recursive function to find solutions to the N queens problem."""
    # Base case if all queens are placed successfully
    # add the solution to the list.
    if row == N:
        solutions.append(queens[:])
        return

    # Try placing the queen in each column of the current row.
    for col in range(N):
        if is_safe(queens, row, col):
            # If it's safe to place the queen
            # add it to the list and move to the next row.
            queens.append([row, col])
            solve_nqueens(queens, row + 1, N, solutions)
            queens.pop()  # Backtrack


def nqueens(N):
    """do a check up before we start solving the problem"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    solve_nqueens([], 0, N, solutions)

    # Print all solutions found.
    for sol in solutions:
        print_solution(sol)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided.
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Solve the N queens problem with the provided value of N.
    nqueens(sys.argv[1])
