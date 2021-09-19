"""
Solution to Secret Handshake task on Exercism.

https://exercism.org/tracks/python/exercises/secret-handshake
"""


def commands(binary_str: str):
    """
    Get list of event for a secret handshake.

    Args:
        binary_str (str): binary number

    Returns:
        list: sequence of events for a secret handshake

    """
    handshake: list = []
    binary: int = int(binary_str, base=2)

    actions = {
        0b1: 'wink',
        0b10: 'double blink',
        0b100: 'close your eyes',
        0b1000: 'jump',
        0b10000: 'reverse',
    }

    for number, action in actions.items():
        if binary & number:
            if action == 'reverse':
                handshake.reverse()
            else:
                handshake.append(action)

    return handshake
