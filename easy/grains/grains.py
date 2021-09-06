def square(number):
    """
    :param number: int - number of square
    :return: int - amount of grains on the square
    """

    if not 0 < number < 65:
        raise ValueError("Invalid square number")

    a, b = 0, 1
    for _ in range(number):
        a, b = b, b * 2
    return a


def total():
    """
    :return: int - total number of grains on the board
    """

    return sum(square(i) for i in range(1, 65))
