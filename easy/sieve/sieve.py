"""
Solution to Sieve of Eratosthenes task on Exercism.

https://exercism.org/tracks/python/exercises/sieve
"""


def primes(limit: int) -> list:
    """
    Get all primes up to and including given limit.

    Args:
        limit: int

    Returns:
        list with all prime numbers from 2 up to and including limit
    """
    prime_numbers: list = list(range(2, limit + 1))
    for number in prime_numbers:
        if number is not None:
            first_multiple = number * 2 - prime_numbers[0]
            for multiple in range(first_multiple, len(prime_numbers), number):
                prime_numbers[multiple] = None

    return [num for num in prime_numbers if num is not None]
