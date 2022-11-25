from unittest import TestCase, main
from ..task_02 import coincidence


class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)), [1, 2, 2.5])

    def test_2(self):
        self.assertEqual(coincidence([1, 2, 3, 4, 5], range(3, 6)), [3, 4, 5])

    def test_3(self):
        self.assertEqual(coincidence([1, 2, 'y', 4, 5], range(2,4)), [2])

    def test_4(self):
        self.assertEqual(coincidence(), [])

    def test_5(self):
        self.assertEqual(coincidence([1, 4, 6]), [])

    def test_6(self):
        self.assertEqual(coincidence([1, 4, 6], range(7, 123)), [])


if __name__ == '__main__':
    main()