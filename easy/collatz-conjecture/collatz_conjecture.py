"""
Solution to Collatz Conjecture task on Exercism

https://exercism.org/tracks/python/exercises/collatz-conjecture
"""

def steps(number):
    """Return number of steps required to reach 1"""

    if number < 1:
        raise ValueError("Number can not be less or equal zero")

    num_of_steps = 0
    while number != 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        num_of_steps += 1
    return num_of_steps
