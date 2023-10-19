from driver import Driver
from raceTime import Time


class GP:

    def __init__(self, name):
        self._name = name
        self._drivers = {}

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def get_name(self, new_name):
        self._name = new_name

    def enter_driver(self, driver: Driver):
        self._drivers.update({driver: [Time(00, 00, 00, 0000), 0]})

    def get_drivers(self):
        return self._drivers

