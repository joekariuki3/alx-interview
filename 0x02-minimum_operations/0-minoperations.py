#!/usr/bin/python3
"""Minumum operation"""

def minOperations(n: int) ->int:
    """function to calculate fewest number of operation
    needed to result in exacty n H characters"""
    if not isinstance(n, int) or n == 1:
        return 0
    if n == 2:
        return 2
    oprations = 0
    remaining = n - 1

    # loop while charachers < n
    #while ()
    # copy and paste operation -> operation =+ 2
    # paste operation -> operation =+ 1
