#!/usr/bin/python3
"""Minimum Number of coins to make change for a given amount"""


def makeChange(coins, total):
    """Make Change Function"""
    if total <= 0:
        return 0

    changeCount = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total == 0:
            break
        # divide total by the coin to see how many of that coin is needed
        changeCount += total // coin
        # append the remainder to get new total
        total %= coin
    # check if new total is 0
    return changeCount if total == 0 else -1
