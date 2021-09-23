"""
Solution to Minesweeper task on Exercism.

https://exercism.org/tracks/python/exercises/minesweeper
"""

from typing import List


def get_neighbours(
    square_x: int, square_y: int, x_max: int, y_max: int,
) -> List[tuple]:
    """
    Get all square's neighbours (max is 8).

    Args:
        square_x (int): square's X position.
        square_y (int): square's Y position.
        x_max (int): field's columns number.
        y_max (int): filed's rows number.

    Returns:
        List[tuple]: list with (x, y) coordinates of square's neighbours.

    """
    neighbours: List[tuple] = []
    for row in range(square_y - 1, square_y + 2):
        for column in range(square_x - 1, square_x + 2):
            if all(
                [
                    row != square_y or column != square_x,
                    column >= 0,
                    column <= x_max - 1,
                    row >= 0,
                    row <= y_max - 1,
                ],
            ):
                neighbours.append((column, row))
    return neighbours


def count_bombs(minefield: List[str], square_x: int, square_y: int) -> int:
    """
    Count bombs around the given square.

    Args:
        minefield (List[str]): field for Minesweeper.
        square_x (int): square's X position.
        square_y (int): square's Y position.

    Returns:
        int: amount of bombs aroung the given square.

    """
    neighbours: List[tuple] = get_neighbours(
        square_x, square_y, len(minefield[0]), len(minefield),
    )
    bomb: str = '*'
    count: int = 0
    for neighbour_x, neighbour_y in neighbours:
        if minefield[neighbour_y][neighbour_x] == bomb:
            count += 1
    return count


def validate_minefield(minefield: List[str]) -> None:
    """
    Validate Minesweeper field.

    Args:
        minefield (List[str]): field for Minesweeper.

    Raises:
        ValueError: rows have different lenghtes.
        ValueError: square is not '*' or ' '

    """
    if len(set(map(len, minefield))) > 1:
        raise ValueError('Mine field is inconsistent')
    for row in minefield:
        for square in row:
            if square not in ' *':
                raise ValueError('Squares must be * or blank')


def get_field_row(minefield: List[str], square_y: int) -> str:
    """
    Get annotated row for Minesweeper field.

    Args:
        minefield (List[str]): field for Minesweeper.
        square_y (int): square's Y position.

    Returns:
        new_row (str): annotated row.

    """
    new_row: str = ''

    for square_x, square in enumerate(minefield[square_y]):
        bombs_count: int = 0
        if square == ' ':
            bombs_count = count_bombs(minefield, square_x, square_y)
        new_row += str(bombs_count) if bombs_count else square

    return new_row


def annotate(minefield: List[str]) -> List[str]:
    """
    Annotate Monesweeper field with bombs count.

    Args:
        minefield (List[str]): field for Minesweeper.

    Returns:
        List[str]: annotated field.

    """
    validate_minefield(minefield)

    for square_y, _ in enumerate(minefield):
        minefield[square_y] = get_field_row(minefield, square_y)
    return minefield
