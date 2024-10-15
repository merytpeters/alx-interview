#!/usr/bin/env python3
"""Minimum operations, fewest number of operations needed"""


def minOperations(n):
    """return the minimum number of operations"""
    if n <= 1:
        return 0

    operations = 0
    for i in range(2, n + 1):
        while n % i == 0:
            operations += i
            n //= i
    return operations
