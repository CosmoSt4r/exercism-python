"""
Solution to Beer Song task on Exercism.

https://exercism.org/tracks/python/exercises/beer-song
"""


def amount_of_bottles(count: int, capital: bool = False) -> str:
    """
    Get line for specified amount of bottles.

    Args:
        count (int): amount of bottles.
        capital (bool): optional, capitalize 'no more'. Defaults to False.

    Returns:
        str: 'N of bottle(s)'.

    """
    word: str = 'bottles'
    amount: str = str(count)
    if count == 0:
        amount = 'No more' if capital else 'no more'
    elif count == 1:
        word = 'bottle'
    return '{0} {1} of beer'.format(amount, word)


def first_line(count: int) -> str:
    """
    Get first line for Beer Song.

    Args:
        count (int): amount of bottles.

    Returns:
        str: first line for Beer Song.

    """
    if count == 0:
        return '{0} on the wall, {1}.'.format(
            amount_of_bottles(0, capital=True), amount_of_bottles(0),
        )
    return '{0} on the wall, {0}.'.format(amount_of_bottles(count))


def second_line(count: int) -> str:
    """
    Get second line for Beer Song.

    Args:
        count (int): amount of bottles.

    Returns:
        str: second line for Beer Song.

    """
    line: str = 'Take one down and pass it around, '
    if count == 0:
        line = 'Go to the store and buy some more, '
        count = 100
    elif count == 1:
        line = 'Take it down and pass it around, '
    return ''.join([line, amount_of_bottles(count - 1), ' on the wall.'])


def recite(start: int, take: int = 1) -> list:
    """
    Generate Beer Song.

    Args:
        start (int): amount of bottles to start from.
        take (int): optional, amount of verses. Defaults to 1.

    Returns:
        list: list with specified amount of verses of Beer Song.

    """
    beer_song = []
    for take_count in range(take):
        beer_song.extend([first_line(start), second_line(start)])
        start = start - 1
        if take_count != take - 1:
            beer_song.append('')
    return beer_song
