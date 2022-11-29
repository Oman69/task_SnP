from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, flavor=None):
        super().__init__()
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    @property
    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        else:
            return True



obj3 = JellyBean()
obj3.flavor = '200'
print(obj3.is_delicious)
obj3.flavor = 'black licorice'
print(obj3.is_delicious)