class Clock:
    def __init__(self, hour, minute):
        self.hours = (hour + minute // 60) % 24
        self.minutes = minute % 60

    def __repr__(self):
        return f"{self.hours:02}:{self.minutes:02}"

    def __eq__(self, other):
        return str(self) == str(other)

    def __add__(self, minutes):
        self.hours += minutes // 60
        self.minutes += minutes % 60

        return Clock(self.hours, self.minutes)

    def __sub__(self, minutes):
        self.hours -= minutes // 60
        self.minutes -= minutes % 60

        return Clock(self.hours, self.minutes)
