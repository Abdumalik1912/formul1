from driver import Driver
from gp import GP


class Championship:

    def __init__(self):
        self._drivers = []
        self._gps = []

    def create_driver(self, name):
        new_driver = Driver(name)
        self._drivers.append(new_driver)
        return new_driver

    def get_drivers(self):
        return self._drivers

    def get_driver(self, name):
        for driver in self._drivers:
            if name == driver.get_name:
                return driver
        return -1.0

    def define_grand_pri(self, name):
        new_gp = GP(name)
        self._gps.append(new_gp)
        return new_gp

    def get_grand_pri(self, name):
        for gp in self._gps:
            if gp.get_name == name:
                return gp
        return -1.0



