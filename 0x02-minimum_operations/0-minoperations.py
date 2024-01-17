#!/usr/bin/python3
"""Minumum operation"""
from typing import Union


def minOperations(n: Union[int, float]) -> int:
    """function to calculate fewest number of operation
    needed to result in exacty n H characters"""
    if not isinstance(n, int):
        return 0
    elif n == 1:
        return 0
    operations = 0

    divider = 2
    while n > 1:
        if not n % divider == 0:
            divider += 1
        n = n / divider
        operations += divider
    return operations
