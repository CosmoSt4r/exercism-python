"""
Solution for Series task on Exercism

https://exercism.org/tracks/python/exercises/series
"""

def slices(series, length):
    """Get all the contiguous substrings of given length in string"""

    if not 0 < length <= len(series):
        raise ValueError("Invalid length of a substring")

    return [series[i:i+length] for i in range(len(series) - length + 1)]
