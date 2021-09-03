from datetime import timedelta


def add(moment):
    """Return the moment that would be after a gigasecond has passed"""
    return moment + timedelta(seconds=10 ** 9)
