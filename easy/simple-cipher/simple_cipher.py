"""
Solution to Simple Cipher task in Exercism

https://exercism.org/tracks/python/exercises/simple-cipher
"""

from random import choice
from itertools import cycle


class Cipher:
    """Implementation of Caesar Cipher"""

    def __init__(self, key: str = None,
                 alphabet: str = "abcdefghijklmnopqrstuvwxyz"):
        self.alphabet = alphabet
        self.key = key if key else self.__generate_key()

    def __generate_key(self, length: int = 100) -> str:
        """Generate random key of given length"""

        return "".join([choice(self.alphabet) for _ in range(length)])

    def __encode_char(self, char: str, key: str) -> str:
        index = self.alphabet.index(char) + self.alphabet.index(key)
        return self.alphabet[index % len(self.alphabet)]

    def __decode_char(self, char: str, key: str) -> str:
        index = (
            len(self.alphabet) + self.alphabet.index(char)
            - self.alphabet.index(key)
        )
        return self.alphabet[index % len(self.alphabet)]

    def encode(self, text: str) -> str:
        """Method for encoding given text"""

        return "".join(
            [
                self.__encode_char(char, k) if char in self.alphabet else char
                for char, k in zip(text, cycle(self.key))
            ]
        )

    def decode(self, text: str) -> str:
        """Method for decoding given text"""

        return "".join(
            [
                self.__decode_char(char, k) if char in self.alphabet else char
                for char, k in zip(text, cycle(self.key))
            ]
        )
