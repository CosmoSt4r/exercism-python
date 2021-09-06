"""
Solution to Phone Number task on Exercism

https://exercism.org/tracks/python/exercises/phone-number
"""

import re


class PhoneNumber:
    """Phone number class"""

    @staticmethod
    def valid(number):
        """Validate phone number"""

        if len(number) != 10:
            return False
        if number[0] in "01" or number[3] in "01":
            return False
        return True

    @staticmethod
    def clean(number):
        """Remove country code, punctuation and whitespaces"""

        number = re.sub(r"[^\w\s]", "", number).replace(" ", "")
        if number[0] == "1":
            number = number[1:]

        if not PhoneNumber.valid(number):
            raise ValueError("Phone number is not valid")
        return number

    def pretty(self):
        """Get prettified phone number"""

        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"

    def __init__(self, number):
        self.number = PhoneNumber.clean(number)
        self.area_code = self.number[:3]
