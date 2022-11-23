from unittest import TestCase, main
from ..task_10 import count_words



class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(count_words("A man man man man, a plan, a canal -- Panama"), {'man': 4, 'a': 3, 'plan': 1, 'canal': 1, 'panama': 1})

    def test_2(self):
        self.assertEqual(count_words('s s'), {'s': 2})

    def test_3(self):
        self.assertEqual(count_words("Doo bee doo bee doo"), {'doo': 3, 'bee': 2})

    def test_4(self):
        self.assertEqual(count_words("Бревно Оно Бревно Моё"), {'бревно': 2, 'оно': 1, 'моё': 1})


if __name__ == '__main__':
    main()