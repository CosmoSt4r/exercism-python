"""
Solution to Flatten Array task on Exercism.

https://exercism.org/tracks/python/exercises/flatten-array
"""

from typing import Iterable


def flatten(nested: Iterable) -> list:
    """
    Flatten nested list.

    Args:
        nested (Iterable): nested list to flatten.

    Returns:
        list: flattened list with all values except None.

    """
    flattened: list = []

    for element in nested:
        if isinstance(element, Iterable):
            flattened.extend(flatten(element))
        elif element is not None:
            flattened.append(element)

    return flattened
