from unittest import TestCase, main
from ..task_08 import multiply_numbers



class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(multiply_numbers('1234'), 24)

    def test_2(self):
        self.assertEqual(multiply_numbers('ss'), None)

    def test_3(self):
        self.assertEqual(multiply_numbers(), None)

    def test_4(self):
        self.assertEqual(multiply_numbers('sssdd34'), 12)

    def test_5(self):
        self.assertEqual(multiply_numbers(2.3), 6)

    def test_6(self):
        self.assertEqual(multiply_numbers([2,3,5]), 30)

    def test_7(self):
        self.assertEqual(multiply_numbers({'key': 123}), 6)


if __name__ == '__main__':
    main()