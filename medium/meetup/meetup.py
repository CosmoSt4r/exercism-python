"""
Solution to Meetup task on Exercism

https://exercism.org/tracks/python/exercises/meetup
"""

import datetime as dt
from calendar import monthrange


class MeetupDayException(Exception):
    """Exception class for invalid meetup dates"""

    def __init__(self, message: str):
        super().__init__()
        self.message: str = message

    def __str__(self) -> str:
        return f"MeetupDayError: {self.message}"


def get_iso_week_day(day_name: str) -> int:
    """Get weekday's ISO number from its name"""

    day_names: tuple = ('monday', 'tuesday', 'wednesday', 'thursday',
                        'friday', 'saturday', 'sunday')
    if day_name.lower() not in day_names:
        raise ValueError("Invalid weekday's name")

    return day_names.index(day_name.lower()) + 1


def meetup(year: int, month: int, week: str, day_of_week: str) -> dt.date:
    """Calculate the date of meetups"""

    iso_day_of_week: int = get_iso_week_day(day_of_week)
    max_days_in_month: int = monthrange(year, month)[1]

    start: int = 0
    end: int = 0
    day_number: int = 1

    if week == 'teenth':
        start, end = 13, 20
    elif week == 'last':
        start, end = max_days_in_month, 0
    else:
        # week == '1st', '2nd', '3rd', '4th', '5th'
        start, end = 1, max_days_in_month + 1
        day_number = int(week[0])

    for day in range(start, end, -1 if start > end else 1):
        date = dt.date(year, month, day)
        if date.isoweekday() == iso_day_of_week:
            day_number -= 1
            if day_number == 0:
                return date
    raise MeetupDayException("Invalid date")
