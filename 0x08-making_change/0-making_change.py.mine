#!/usr/bin/python3
"""script to find minumum number of coins we can use to make change
"""

from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """using coins provided,
    make change of total with minimum number of coins
    Return Minimum number of coins or -1
    """
    if total <= 0:
        return 0

    max_coin = max(coins)
    changes = [max_coin + 1] * (total + 1)
    changes[0] = 0
    for coin in coins:
        for amount in range(coin, total + 1):
            changes[amount] = min(changes[amount], changes[amount - coin] + 1)
    if changes[total] == max_coin + 1:
        return -1
    return changes[total]
