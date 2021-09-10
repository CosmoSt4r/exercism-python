"""
Solution for Saddle Points task on Exercism

https://exercism.org/tracks/python/exercises/saddle-points
"""

def check_for_saddle(element: int, row: list, column: list):
    """Check if point is saddle"""

    for num in row:
        if element < num:
            return False
    for num in column:
        if element > num:
            return False
    return True


def saddle_points(matrix: list) -> list:
    """Identify all saddle points in matrix"""

    if len(set(map(len, matrix))) > 1:
        # If lengths of rows differ raise error
        raise ValueError("Matrix is invalid")

    points: list = []
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            if check_for_saddle(element, row, [matrix[x][j] for x in range(len(matrix))]):
                points.append({"row": i + 1, "column": j + 1})
    return points
