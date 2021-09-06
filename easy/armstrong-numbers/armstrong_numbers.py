"""
Solution for Armstrong Numbers task on Exercism

https://exercism.org/tracks/python/exercises/armstrong-numbers
"""

def is_armstrong_number(number):
    """
    Determine whether the number is Armstrong number or not

    An Armstrong number is a number that is the sum of its
    own digits each raised to the power of the number of digits
    """
    return sum([int(x)**len(str(number)) for x in str(number)]) == number
