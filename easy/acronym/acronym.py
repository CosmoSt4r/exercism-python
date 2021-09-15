"""
Solution to Acronym task on Exercism.

https://exercism.org/tracks/python/exercises/acronym
"""
import re


def abbreviate(phrase: str) -> str:
    """Convert a phrase to its acronym.

    Args:
        phrase: string with words

    Returns:
        acronym for given phrase
    """
    words: list = re.sub(r'[_+\,+\-+]', ' ', phrase).split()
    return ''.join(word[0].upper() for word in words)
