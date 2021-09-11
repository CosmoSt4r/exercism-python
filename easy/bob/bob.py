"""
Solution to Bob task on Exercism

https://exercism.org/tracks/python/exercises/bob
"""

def response(hey_bob: str) -> str:
    """Get Bob's answer"""

    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.lower() != hey_bob and hey_bob.upper() == hey_bob:
        if hey_bob[-1] == '?':
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if hey_bob[-1] == '?':
        return "Sure."
    return "Whatever."
