"""
Solution to OCR Numbers task on Exercism.

https://exercism.org/tracks/python/exercises/ocr-numbers
"""


def recognize_number(str_number: str) -> str:
    """
    Recognize number from its grid representation.

    Args:
        str_number (str): number representation on grid.

    Returns:
        str: recognized decimal number or '?'.

    """
    str_to_number = {
        ' _ | ||_|': '0',
        '     |  |': '1',
        ' _  _||_ ': '2',
        ' _  _| _|': '3',
        '   |_|  |': '4',
        ' _ |_  _|': '5',
        ' _ |_ |_|': '6',
        ' _   |  |': '7',
        ' _ |_||_|': '8',
        ' _ |_| _|': '9',
        '         ': ',',
    }
    if str_to_number.get(str_number):
        return str_to_number.get(str_number)
    return '?'


def separate_numbers(input_grid: list) -> list:
    """
    Separate numbers on grid.

    Args:
        input_grid (list): grid with numbers.

    Returns:
        list: separated numbers (length=3x4=12 for each).

    """
    separated_numbers = []
    for row in range(0, len(input_grid), 4):
        for col in range(0, len(input_grid[0]), 3):
            single_number = '{0}{1}{2}'.format(
                input_grid[row][col:3 + col],
                input_grid[row + 1][col:3 + col],
                input_grid[row + 2][col:3 + col],
            )
            separated_numbers.append(single_number)

        if row + 4 < len(input_grid):
            separated_numbers.append(' ' * 9)

    return separated_numbers


def validate_grid(input_grid: list) -> None:
    """
    Validate numbers grid.

    Args:
        input_grid (list): grid with numbers.

    Raises:
        ValueError: if grid has incorrect size.

    """
    length = len(''.join(input_grid))
    if length % 3 != 0 or length % 4 != 0:
        raise ValueError('Grid is invalid')


def convert(input_grid: list) -> str:
    """
    Convert numbers grid to decimal numbers.

    Args:
        input_grid (list): grid with numbers.

    Returns:
        str: decimal representation of numbers on the grid.

    """
    validate_grid(input_grid)
    str_numbers: list = separate_numbers(input_grid)
    return ''.join([recognize_number(number) for number in str_numbers])
