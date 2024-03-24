#!/usr/bin/python3
"""alx-interview
   Task: Minimum Operations
"""


def minOperations(n):
    """Find minimum operations needed to arrive at n H's
    """
    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n /= factor

        factor += 1

    return operations
