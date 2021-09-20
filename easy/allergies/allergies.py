"""
Solution to Allergies task on Exercism.

https://exercism.org/tracks/python/exercises/allergies
"""


class Allergies(object):
    """Allergies class."""

    allergies = (
        'eggs',
        'peanuts',
        'shellfish',
        'strawberries',
        'tomatoes',
        'chocolate',
        'pollen',
        'cats',
    )

    def __init__(self, score: int):
        """
        Initialize Allergies object.

        Args:
            score (int): allergies score.

        """
        self.max_score = 256
        self.lst = score

    def allergic_to(self, allergen: int) -> bool:
        """
        Check if person is allergic to given allergen.

        Args:
            allergen (int): object that can cause allergy.

        Returns:
            bool: true if person is allergic to given allergen.

        """
        return allergen in self.lst

    @property
    def lst(self) -> list:
        """
        Get list of allergies.

        Returns:
            list: list of allergies person is allergic to.

        """
        return self._lst

    @lst.setter
    def lst(self, score: int) -> None:
        """
        Set list of allergies from person's allergy score.

        Args:
            score (int): person's allergy score.

        """
        self._lst: list = []
        score %= self.max_score

        for index in range(7, -1, -1):
            allergen_value = 2**index
            if allergen_value <= score:
                score -= allergen_value
                self._lst.append(self.allergies[index])
            if score == 0:
                break
