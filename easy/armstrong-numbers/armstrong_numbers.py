"""
Solution for Armstrong Numbers task on Exercism.

https://exercism.org/tracks/python/exercises/armstrong-numbers
"""


def get_armstrong_value(number: int) -> int:
    """
    Get Armstrong number of given number.

    Armstrong value of a number is the sum of its digits
    each raised to the power of the number of its digits.

    Args:
        number (int): input number.

    Returns:
        int: Armstrong value of given number.

    """
    armstrong_value: list = []
    number_len: int = len(str(number))

    for digit in str(number):
        armstrong_value.append(int(digit) ** number_len)
    return sum(armstrong_value)


def is_armstrong_number(number: int) -> bool:
    """
    Determine whether the number is Armstrong number or not.

    An Armstrong number is a number that is the sum of its
    own digits each raised to the power of the number of digits

    Args:
        number (int): number to check.

    Returns:
        bool: True if number is Armstrong number.

    """
    return get_armstrong_value(number) == number
