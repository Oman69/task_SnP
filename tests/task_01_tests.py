from unittest import TestCase, main
from ..task_01 import is_palindrome


class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(is_palindrome('2+2'), True)

    def test_2(self):
        self.assertEqual(is_palindrome('767'), True)

    def test_3(self):
        self.assertEqual(is_palindrome("A man, a plan, a canal -- Panama"), True)

    def test_4(self):
        self.assertEqual(is_palindrome("Madam, I'm Adam!"), True)

    def test_5(self):
        self.assertEqual(is_palindrome(None), False)

    def test_6(self):
        self.assertEqual(is_palindrome("Боров!"), False)

    def test_7(self):
        self.assertEqual(is_palindrome("/ТоПоТ..."), True)


if __name__ == '__main__':
    main()