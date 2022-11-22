from unittest import TestCase, main
from ..task_04 import sort_list


class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(sort_list([2, 4, 6, 8]), [8, 4, 6, 2, 2])

    def test_2(self):
        self.assertEqual(sort_list([1, 2, 1, 3]), [3, 2, 3, 1, 1])

    def test_3(self):
        self.assertEqual(sort_list([1]), [1, 1])

    def test_4(self):
        self.assertEqual(sort_list(), [])

    def test_5(self):
        self.assertEqual(sort_list([]), [])