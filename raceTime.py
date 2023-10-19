class Time:

    def __init__(self, hours, minutes, seconds, milliseconds):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._milliseconds = milliseconds

    @property
    def get_hours(self):
        return self._hours

    @get_hours.setter
    def get_hours(self, new_hours):
        self._hours = new_hours

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, new_minutes):
        self._minutes = new_minutes

    @property
    def seconds(self):
        return self._seconds

    @property
    def milliseconds(self):
        return self._milliseconds

    def to_string(self):
        return f"{self._hours}:{self._minutes}:{self._seconds}:{self._milliseconds}"

