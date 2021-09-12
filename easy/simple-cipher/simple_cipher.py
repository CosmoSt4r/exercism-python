"""
Solution to Simple Cipher task in Exercism

https://exercism.org/tracks/python/exercises/simple-cipher
"""

from random import choice
from itertools import cycle


class Cipher:
    """Implementation of Caesar Cipher"""

    __alphabet: str = "abcdefghijklmnopqrstuvwxyz"

    @classmethod
    def generate_key(cls, length: int = 100) -> str:
        """Generate random key of given length"""

        return "".join([choice(cls.__alphabet) for _ in range(length)])

    def __init__(self, key: str = None):
        self.key = key if key else self.generate_key()

    def __encode_char(self, char: str, key: str) -> str:
        return self.__alphabet[
            (self.__alphabet.index(char) + self.__alphabet.index(key))
            % len(self.__alphabet)
        ]

    def __decode_char(self, char: str, key: str) -> str:
        return self.__alphabet[
            (
                len(self.__alphabet)
                + self.__alphabet.index(char)
                - self.__alphabet.index(key)
            )
            % len(self.__alphabet)
        ]

    def encode(self, text: str) -> str:
        """Method for encoding given text"""

        return "".join(
            [
                self.__encode_char(char, k) if char in self.__alphabet else char
                for char, k in zip(text, cycle(self.key))
            ]
        )

    def decode(self, text: str) -> str:
        """Method for decoding given text"""

        return "".join(
            [
                self.__decode_char(char, k) if char in self.__alphabet else char
                for char, k in zip(text, cycle(self.key))
            ]
        )
