"""
Solution to Difference of Squares task on Exercism.

https://exercism.org/tracks/python/exercises/difference-of-squares
"""


def square_of_sum(number: int) -> int:
    """
    Get square of sum of the first N numbers.

    Args:
        number (int): limit.

    Returns:
        int: square of sum of the first N numbers.

    """
    return sum(range(1, number + 1))**2


def sum_of_squares(number: int) -> int:
    """
    Get sum of squares of the first N numbers.

    Args:
        number (int): limit.

    Returns:
        int: sum of squares of the first N numbers.

    """
    return sum([num**2 for num in range(1, number + 1)])


def difference_of_squares(number: int) -> int:
    """
    Get the difference between square of sum and sum of squares.

    Args:
        number (int): limit.

    Returns:
        int: difference between square of sum and sum of squares.

    Raises:
        ValueError: if number less than or equal to zero.

    """
    if number <= 0:
        raise ValueError('Number can not be less than or equal to zero')

    return square_of_sum(number) - sum_of_squares(number)
