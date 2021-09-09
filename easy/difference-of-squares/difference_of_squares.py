"""
Solution to Difference of Squares task on Exercism

https://exercism.org/tracks/python/exercises/difference-of-squares
"""

def square_of_sum(number):
    """Return square of sum of the first N numbers"""
    return sum(range(1, number + 1))**2


def sum_of_squares(number):
    """Return sum of squares of the first N numbers"""
    return sum([i**2 for i in range(1, number + 1)])


def difference_of_squares(number):
    """
    Return the difference between square of sum and
    sum of squares of the first N numbers
    """

    if number <= 0:
        raise ValueError("Number can not be less than or equal to zero")

    return square_of_sum(number) - sum_of_squares(number)
