#!/usr/bin/python3
"""Minimum Number of coins to make change for a given amount"""


def makeChange(coins, total):
    """Make Change Function"""
    if total <= 0:
        return 0

    changeCount = 0
    coins.sort(reverse=True)
    for coin in coins:
        while total >= coin:
            total -= coin
            changeCount += 1

        if total == 0:
            return changeCount
    return -1
