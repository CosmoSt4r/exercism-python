"""
Solution to Collatz Conjecture task on Exercism.

https://exercism.org/tracks/python/exercises/collatz-conjecture
"""


def apply_collatz(number: int) -> int:
    """
    Apply one step of Collatz Conjecture.

    Args:
        number (int): number to apply Collatz Conjecture to.

    Returns:
        int: number after applying one step of Collatz Conjecture.

    """
    if number % 2 == 0:
        return number / 2
    return number * 3 + 1


def steps(number: int) -> int:
    """
    Return number of steps required to reach 1.

    Args:
        number (int): number to apply Collatz Conjecture to.

    Returns:
        int: number of steps required to reach 1.

    Raises:
        ValueError: if number is less than 1.
    """
    if number < 1:
        raise ValueError('Number can not be less or equal zero')

    num_of_steps: int = 0
    while number != 1:
        number = apply_collatz(number)
        num_of_steps += 1
    return num_of_steps
