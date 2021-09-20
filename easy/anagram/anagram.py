"""
Solution for Anagram task on Exercism.

https://exercism.org/tracks/python/exercises/anagram
"""


from collections import Counter


def is_anagram(word: str, candidate: str) -> bool:
    """
    Check if word is anagram of candidate.

    Args:
        word (str): word to check if it's an anagram of candidate.
        candidate (str): candidate to anagram.

    Returns:
        bool: True if word is anagram of candidate.
    """
    word, candidate = word.lower(), candidate.lower()
    return Counter(word) == Counter(candidate) and word != candidate


def find_anagrams(word: str, candidates: list) -> list:
    """
    Get list of words from candidates that is anagram to word.

    Args:
        word (str): word to check for anagram.
        candidates (list): list with candidates for anagram to word.

    Returns:
        list: list with anagrams to given word.

    """
    return list(
        filter(lambda candidate: is_anagram(word, candidate), candidates),
    )
