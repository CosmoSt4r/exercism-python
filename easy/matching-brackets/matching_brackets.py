"""
Solution to Matching Brackets task on Exercism

https://exercism.org/tracks/python/exercises/matching-brackets
"""


def is_paired(input_string: str):
    """Check if brackets in string are matching"""

    stack: list = []
    brackets: str = "(){}[]"

    for char in input_string:
        if char in brackets:
            index = brackets.index(char)
            if index % 2 == 0:
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop(-1) != brackets[index - 1]:
                    return False
    return len(stack) == 0
