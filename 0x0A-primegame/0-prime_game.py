#!/usr/bin/python3
"""Prime Game"""


def isprime(n):
    """Checks for prime numbers using sieve of eratosthene
    and returns the prime number and all its multiples"""
    prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = [p for p in range(2, n+1) if prime[p]]
    return primes


def isWinner(x, nums):
    """Function that returns the winner in a prime game where players
    alternate picking prime numbers and their multiple"""
    precomputed_primes = isprime(10000)
    maria = 0
    ben = 0

    while x > 0:
        for n in nums:
            # Simulate game for each round
            prime_nums = [p for p in precomputed_primes if p <= n]
            # A set of primes for fast lookup
            prime_set = set(prime_nums)
            turns = 0

            while prime_set:
                # Maria's turn, as first player
                # Maria picks the smallest prime
                prime = min(prime_set)
                # Remove prime and multiples
                prime_set.difference_update(range(prime, n + 1, prime))
                turns += 1

                if not prime_set:
                    break

                # Ben picks the smallest prime
                prime = min(prime_set)
                prime_set.difference_update(range(prime, n + 1, prime))
                turns += 1

            # Maria wins if turns is odd
            if turns % 2 == 1:
                maria += 1
            else:
                ben += 1
        x -= 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
