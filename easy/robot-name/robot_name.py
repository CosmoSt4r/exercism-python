"""
Solution for Robot Name task on Exercism

https://exercism.org/tracks/python/exercises/robot-name
"""

from random import randint

class Robot:
    """Robot class"""

    names = []

    @classmethod
    def __generate_name(cls):
        """
        Class method to generate new name for a robot

        Generates name with two uppercase letters and a random 3-digit number
        Adds new name to existing list of names and returns it
        """

        while True:
            name = f'{chr(randint(65, 90))}{chr(randint(65, 90))}{randint(0, 999):03}'
            if name not in cls.names:
                cls.names.append(name)
                break
        return name


    def __init__(self):
        self.name = self.__generate_name()


    def reset(self):
        """Method to reset the robot's state"""

        self.__init__()


    def greet(self):
        """Method to get greeting from a robot"""

        return f"Hello! My name is {self.name}."
