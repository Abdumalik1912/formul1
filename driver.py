class Driver:

    def __init__(self, name):
        self._name = name

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def get_name(self, new_name):
        self._name = new_name

