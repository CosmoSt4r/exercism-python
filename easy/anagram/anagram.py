"""
Solution for Anagram task on Exercism

https://exercism.org/tracks/python/exercises/anagram
"""
from collections import Counter


def find_anagrams(word, candidates):
    """Get list of words from candidates that is anagram to word"""

    return list(
        filter(
            lambda x: Counter(x.lower()) == Counter(word.lower())
            and x.lower() != word.lower(),
            candidates,
        )
    )
