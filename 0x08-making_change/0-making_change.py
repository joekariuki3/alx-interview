#!/usr/bin/python3
"""script to find min number of coins needed to make a certain amount
"""


def makeChange(coins, total):
    """Return min number of coins to make total
    """
    if total <= 0:
        return 0
    count = 0

    # sort the coins from largest to smallest
    coins = sorted(coins, reverse=True)

    # loop over each coin
    for coin in coins:
        # when total is geater than current coin
        # use the coin as much as possible
        while total >= coin:
            # reduce the total with current coin
            total = total - coin

            # count the number of coins used
            count = count + 1

            # if total is 0 no need to continue
            # we have our required coins break the inner loop
            if total == 0:
                break

        # same here break outer loop
        if total == 0:
            break

    # if total is not 0 means we are not able to make the change
    if total != 0:
        return -1
    return count
