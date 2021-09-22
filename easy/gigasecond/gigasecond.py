"""
Solution to Gigasecond task on Exercism.

https://exercism.org/tracks/python/exercises/gigasecond
"""

from datetime import timedelta


def add(moment):
    """
    Get the moment that would be after a gigasecond has passed.

    Args:
        moment: current datetime.

    Returns:
        datetime after a gigasecond has passed.

    """
    return moment + timedelta(seconds=10 ** 9)
