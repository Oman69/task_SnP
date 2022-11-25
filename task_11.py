class Food:
    pass


class Desert:
    def __init__(self, name=None, calories=0):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        self._calories = value

    @property
    def is_healthy(self):
        if self._calories < 200:
            return True
        else:
            return False

    @property
    def is_delicious(self):
        if isinstance(self, Desert):
            return True
