class Time:

    def __init__(self, hours, minutes, seconds, milliseconds):
      self._hours = hours
      self._minutes = minutes
      self._seconds = seconds
      self._milliseconds = milliseconds

    def to_string(self):
      return f"{self._hours}:{self._minutes}:{self._seconds}:{self._milliseconds}"
