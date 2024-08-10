#!/usr/bin/python3
"""Module defining isWinner function."""


def sieve_of_eratosthenes(max_n):
    """
    Generates a list of boolean values indicating whether
    each number up to max_n is a prime number.

    Parameters:
    max_n (int): The upper limit of numbers to check for primality.

    Returns:
    list: A list of boolean values where the index represents
    the number, and the value is True if it's a prime.
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, max_n + 1, i):
                is_prime[j] = False
    return is_prime


def isWinner(x, nums):
    """
    Determines the winner of a series of rounds in a game where
    Maria and Ben take turns removing prime numbers
    and their multiples from a set of integers.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list): A list of integers where each integer represents
    the upper limit of the set for that round.

    Returns:
    str: The name of the player that won the most rounds
    ("Maria" or "Ben"), or None if the winner cannot be determined.
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)

    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_removed = 0

        for i in range(2, n + 1):
            if is_prime[i]:
                primes_removed += 1

        if primes_removed % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
