"""
Solution to Triangle task on Exercism

https://exercism.org/tracks/python/exercises/triangle
"""

def validate_triangle(sides: list) -> bool:
    """Check if triangle is valid"""

    if 0 in sides:
        return False
    if sum(sides[:2]) < sides[2]\
    or sum([sides[0], sides[2]]) < sides[1]\
    or sum(sides[1:]) < sides[0]:
        return False
    return True


def equilateral(sides: list) -> bool:
    """Check if triangle is equilateral"""

    return validate_triangle(sides) and len(set(sides)) == 1


def isosceles(sides: list) -> bool:
    """Check if triangle is isosceles"""

    return validate_triangle(sides) and len(set(sides)) <= 2


def scalene(sides: list) -> bool:
    """Check if triangle is scalene"""

    return validate_triangle(sides) and len(set(sides)) == 3
