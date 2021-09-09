"""
Solution to ISBN Verifier task on Exercism

https://exercism.org/tracks/python/exercises/isbn-verifier
"""

def is_valid(isbn: str) -> bool:
    """Check if provided string is a valid ISBN-10"""

    isbn = list(isbn.replace('-', '').replace(' ', ''))

    if not isbn:
        return False

    if isbn[-1] == 'X':
        isbn[-1] = '10'

    if len(isbn) != 10 or not ''.join(isbn).isdigit():
        return False

    return sum([i * num for i, num in zip(range(10, 0, -1), map(int, isbn))]) % 11 == 0
