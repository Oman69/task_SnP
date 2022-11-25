from unittest import TestCase, main
from ..task_09 import connect_dicts


class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}), {'c': 11, 'b': 12})

    def test_2(self):
        self.assertEqual(connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}), {'d': 11, 'c': 12, 'a': 13})

    def test_3(self):
        self.assertEqual(connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}), {'c': 11, 'b': 12, 'a': 15})


if __name__ == '__main__':
    main()
