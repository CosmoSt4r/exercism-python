"""
Solution to Allergies task on Exercism

https://exercism.org/tracks/python/exercises/allergies
"""

class Allergies:
    """Allergies class"""

    allergies = (
        'eggs', 'peanuts', 'shellfish', 'strawberries',
        'tomatoes', 'chocolate', 'pollen', 'cats',
        )

    def __init__(self, score: int):
        self.lst = score

    def allergic_to(self, item: int) -> bool:
        """Return True if person is allergic to given item"""

        return item in self._lst

    @property
    def lst(self) -> list:
        """Get list of allergies"""

        return self._lst

    @lst.setter
    def lst(self, score: int) -> None:
        """Set list of all allergies a person have based on score"""

        self._lst: list = []
        score %= 256

        for value, index in ((2**x, x) for x in range(7, -1, -1)):
            if value <= score:
                score -= value
                self._lst.append(self.allergies[index])
            if score == 0:
                break
