"""
Solution to Prefect Numbers task on Exercism

https://exercism.org/tracks/python/exercises/perfect-numbers
"""


def classify(number):
    """
    Determine if a number is perfect, abundant,
    or deficient based on Nicomachus' classification
    scheme for positive integers.
    """

    if number <= 0:
        raise ValueError("Positive numbers only")

    factors_sum = sum({x for x in range(1, number) if number % x == 0})

    if factors_sum == number:
        return "perfect"
    if factors_sum > number:
        return "abundant"
    return "deficient"
