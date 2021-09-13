"""
Solution to Sum of Multiples task on Exercism

https://exercism.org/tracks/python/exercises/sum-of-multiples
"""

def sum_of_multiples(limit: int, multiples: list):
    """Get the sum of all unique multiples of
    particular numbers"""

    result: int = 0
    for i in range(1, limit):
        for num in multiples:
            if num != 0 and i % num == 0:
                result += i
                break
    return result
