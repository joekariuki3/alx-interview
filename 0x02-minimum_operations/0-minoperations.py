#!/usr/bin/python3
"""Minumum operation"""


def minOperations(n: int) -> int:
    """function to calculate fewest number of operation
    needed to result in exacty n H characters"""

    copy = 1
    paste = 1
    current_char = 1
    operations = 0
    """holds current_chars (one to paste if no latest copy has been done)"""
    clipboard = current_char

    """check if n is int"""
    if not isinstance(n, int) or n == 1:
        return operations
    while current_char < n:
        """get remaining chars"""
        remaining_char = n - current_char

        """check if we copy n paste current chars we will exced remaining_char
        if not do copy then past (2 operations)"""
        if (remaining_char % current_char == 0):
            """copy the characters and paste"""
            clipboard = current_char  # copy operation
            current_char += clipboard  # paste operation
            """increment copy n paste operation"""
            operations = operations + copy + paste
        else:
            """if there will be a remainder
            just do a paste (1 operation) paste"""
            current_char += clipboard  # paste operation
            operations += paste  # increment paste operation
    return operations
