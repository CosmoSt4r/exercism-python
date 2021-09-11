"""
Solution to Prime Factors task on Exercism

https://exercism.org/tracks/python/exercises/prime-factors
"""

def is_prime(value: int) -> bool:
    """Check if value is prime"""

    if value == 1:
        return False
    if value <= 0:
        raise ValueError("Value must be greater than zero")

    for i in range(2, int(value**(1/2)) + 1):
        if value % i == 0:
            return False
    return True


def factors(value: int) -> list:
    """Get all prime factors of the given value"""

    prime_factors: list = []

    for i in range(2, value + 1):
        if i > 2 and i % 2 == 0 or not is_prime(i):
            continue

        while value % i == 0:
            value = int(value / i)
            prime_factors.append(i)

        if value == 1:
            break

    return prime_factors
