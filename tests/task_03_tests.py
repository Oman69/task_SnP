from unittest import TestCase, main
from ..task_03 import max_odd


class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(max_odd([1, 2, 3, 4, 4]), 3)

    def test_2(self):
        self.assertEqual(max_odd([21.0, 2, 3, 4, 4]), 21)

    def test_3(self):
        self.assertEqual(max_odd(['ololo', 2, 3, 4, [1, 2], None]), 3)

    def test_4(self):
        self.assertEqual(max_odd(['ololo', 'fufufu']), None)

    def test_5(self):
        self.assertEqual(max_odd([2, 2, 4]), None)