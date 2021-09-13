"""
Solution to Complex Numbers task on Exercism

https://exercism.org/tracks/python/exercises/complex-numbers
"""

from __future__ import annotations
import math


class ComplexNumber:
    """Class for Complex Numbers"""

    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __str__(self) -> str:
        if not self.real and not self.imaginary:
            return "0"

        real: str = str(self.real) if self.real else ''
        sign: str = '+' if self.imaginary > 0 and self.real != 0 else ''
        imag: str = str(self.imaginary) if self.imaginary not in (
            1, -1, 0) else ''
        i: str = 'i' if self.imaginary != 0 else ''

        return f"{real}{sign}{imag}{i}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComplexNumber):
            return NotImplemented
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def __mul__(self, other: ComplexNumber) -> ComplexNumber:
        real: float = self.real * other.real - self.imaginary * other.imaginary
        imag: float = self.imaginary * other.real + self.real * other.imaginary
        return ComplexNumber(real, imag)

    def __sub__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(self.real - other.real,
                             self.imaginary - other.imaginary)

    def __truediv__(self, other: ComplexNumber) -> ComplexNumber:
        real: float = self.real * other.real + self.imaginary * other.imaginary
        imag: float = self.imaginary * other.real - self.real * other.imaginary
        mod: float = math.pow(abs(other), 2)
        return ComplexNumber(real / mod, imag / mod)

    def __abs__(self) -> float:
        return math.pow(
            math.pow(self.real, 2) + math.pow(self.imaginary, 2), 1/2)

    def conjugate(self) -> ComplexNumber:
        """Get conjugate for complex number"""

        return ComplexNumber(self.real, -self.imaginary)

    def exp(self) -> ComplexNumber:
        """Get e to the power of complex number"""

        mult: float = pow(math.e, self.real)
        real: float = math.cos(self.imaginary)
        imag: float = math.sin(self.imaginary)
        return ComplexNumber(mult * real, mult * imag)
