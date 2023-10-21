from driver import Driver
from gp import GP
from raceTime import Time


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

    def enter_driver(self, gp: GP, driver: Driver):
        for gps in self._gps:
            if gps == gp:
                gps.enter_driver(driver)
                driver.add_race(gp)
                return "Driver has entered the Grand Pri"
        return -1.0

    def gp_ranking(self, gp: GP):
        for gps in self._gps:
            if gps == gp:
                return gps.gp_ranking()
        return -1.0

    def get_position(self, driver: Driver, gp: GP):
        for gps in self._gps:
            if gps == gp:
                return gps.get_position(driver)
        return "No such Grand Pri"

    @staticmethod
    def add_position(gp: GP, dr: Driver, place: int):
        dr.get_races()[gp][0] = place
        if place == 1:
            dr.get_races()[gp][1] = 25
        elif place == 2:
            dr.get_races()[gp][1] = 18
        elif place == 3:
            dr.get_races()[gp][1] = 15
        elif place == 4:
            dr.get_races()[gp][1] = 12
        elif place == 5:
            dr.get_races()[gp][1] = 10
        elif place == 6:
            dr.get_races()[gp][1] = 8
        elif place == 7:
            dr.get_races()[gp][1] = 6
        elif place == 8:
            dr.get_races()[gp][1] = 4
        elif place == 9:
            dr.get_races()[gp][1] = 2
        elif place == 10:
            dr.get_races()[gp][1] = 1

    def set_time(self, gp: GP, driver: Driver, hour, minute, second, millisecond):
        for gps in self._gps:
            if gp == gps:
                finish_time = Time(hour, minute, second, millisecond)
                for dr in gp.get_drivers():
                    if dr == driver:
                        gp.get_drivers()[driver][0] = finish_time
                        rank = 0
                        for dr2 in gp.get_drivers():
                            if dr2 != driver and gp.get_drivers()[dr2][1] != 0:
                                rank += 1
                                if gp.get_drivers()[driver][0].get_hours < gp.get_drivers()[dr2][0].get_hours:
                                    gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = gp.get_drivers()[dr2][1], \
                                                                                            gp.get_drivers()[dr2][1] + 1
                                    self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                elif gp.get_drivers()[driver][0].get_hours == gp.get_drivers()[dr2][0].get_hours:
                                    if gp.get_drivers()[driver][0].minutes < gp.get_drivers()[dr2][0].minutes:
                                        gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = gp.get_drivers()[dr2][
                                                                                                    1], \
                                                                                                gp.get_drivers()[dr2][
                                                                                                    1] + 1
                                        self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                    elif gp.get_drivers()[driver][0].minutes == gp.get_drivers()[dr2][0].minutes:
                                        if gp.get_drivers()[driver][0].seconds < gp.get_drivers()[dr2][0].seconds:
                                            gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = \
                                                gp.get_drivers()[dr2][
                                                    1], \
                                                gp.get_drivers()[dr2][
                                                    1] + 1
                                            self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                        elif gp.get_drivers()[driver][0].seconds == gp.get_drivers()[dr2][
                                            0].seconds:
                                            if gp.get_drivers()[driver][0].milliseconds < gp.get_drivers()[dr2][
                                                0].milliseconds:
                                                gp.get_drivers()[driver][1], gp.get_drivers()[dr2][1] = \
                                                    gp.get_drivers()[dr2][
                                                        1], \
                                                    gp.get_drivers()[dr2][
                                                        1] + 1
                                                self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                            elif gp.get_drivers()[driver][0].milliseconds == gp.get_drivers()[dr2][
                                                0].milliseconds:
                                                gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1]
                                                self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                            else:
                                                gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                                self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                        else:
                                            gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                            self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                    else:
                                        gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                        self.add_position(gp, driver, gp.get_drivers()[driver][1])
                                else:
                                    gp.get_drivers()[driver][1] = gp.get_drivers()[dr2][1] + 1
                                    self.add_position(gp, driver, gp.get_drivers()[driver][1])
                        if rank == 0:
                            gp.get_drivers()[driver][1] = 1
                            self.add_position(gp, driver, gp.get_drivers()[driver][1])
                            return finish_time
                        else:
                            return finish_time
                return "No such driver"
        return "No such Grand Pri"
