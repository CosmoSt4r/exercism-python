"""
Solution to Largest Series Product task on Exercism

https://exercism.org/tracks/python/exercises/largest-series-product
"""

from functools import reduce


def slices(series: str, length: int) -> list:
    """Get all the contiguous substrings of given length in string"""

    if not 0 < length <= len(series):
        raise ValueError("Invalid length of a substring")

    return [series[i : i + length] for i in range(len(series) - length + 1)]


def product(number: str) -> int:
    """Get product of all digits in given number"""

    return reduce(lambda a, b: int(a) * int(b), number)


def largest_product(series: str, size: int) -> int:
    """
    Get the largest product for a contiguos
    substring of digits of length n
    """

    if size == 0:
        return 1
    series = slices(series, size)
    return max([product(number) for number in series])
