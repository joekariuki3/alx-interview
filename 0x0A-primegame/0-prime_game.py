#!/usr/bin/python3
"""Prime Game
"""


def is_prime(i):
    """checks if a number is prime
    """
    if i <= 1:
        return False
    if i <= 3:
        return True
    if i % 2 == 0 or i % 3 == 0:
        return False
    x = 5
    while x * x <= i:
        if i % x == 0 or i % (x + 2) == 0:
            return False
        x += 6
    return True


def get_primes(n):
    """generate prime numbers up to n
    """
    prime_nums = []
    for i in range(2, n+1):
        if is_prime(i):
            prime_nums.append(i)
    return prime_nums


def isWinner(x, nums):
    """return the winner of the game
    """
    maria = 0
    ben = 0

    for n in nums:
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if maria > ben:
        return 'Maria'
    elif maria < ben:
        return 'Ben'
    else:
        return None