from unittest import TestCase, main
from ..task_11 import Dessert
from ..task_12 import JellyBean

obj1 = Dessert()
obj3 = JellyBean()


class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(obj1.is_healthy, True)

    def test_2(self):
        self.assertEqual(obj1.is_delicious, True)

    def test_3(self):
        obj1.calories = 220
        self.assertEqual(obj1.is_healthy, False)

    def test_4(self):
        obj3.flavor = 'Lime'
        self.assertEqual(obj3.flavor, 'Lime')

    def test_5(self):
        obj3.flavor = 'black licorice'
        self.assertEqual(obj3.is_delicious, False)

    def test_6(self):
        obj3.calories = 300
        self.assertEqual(obj3.is_healthy, False)


if __name__ == '__main__':
    main()


