
class Named:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = str(name)

