from unittest import TestCase, main
from ..task_11 import Desert, Food

obj1 = Desert()
obj2 = Food()

class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(obj1.is_healthy, True)

    def test_2(self):
        self.assertEqual(obj1.is_delicious, True)

    def test_3(self):
        obj1.calories = 220
        self.assertEqual(obj1.is_healthy, False)


