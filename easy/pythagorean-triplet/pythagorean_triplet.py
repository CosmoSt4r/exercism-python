"""
Solution to Pythagorean Triplet task on Exercism

https://exercism.org/tracks/python/exercises/pythagorean-triplet
"""


def triplets_with_sum(number: int) -> list:
    """Get all pythagorean triplets which in sum give number"""

    result = []
    for a in range(1, number // 3):
        for b in range(a + 1, (number // 3) * 2):
            c = number - a - b
            if a + b < c or a * a + b * b != c * c:
                continue
            result.append([a, b, c])
    return result
