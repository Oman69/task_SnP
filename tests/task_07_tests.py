from unittest import TestCase, main
from ..task_07 import combine_anagrams



class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]), [['cars', 'racs', 'scar'], ['for'], ['potatoes'], ['four'], ['creams', 'scream']])

    def test_2(self):
        self.assertEqual(combine_anagrams(["Топот", "потоп", "Potatoes", "racs", "four", "scar", "Creams", "Scream"]), [['Топот'], ['потоп'], ['Potatoes'], ['racs', 'scar'], ['four'], ['Creams', 'Scream']])



if __name__ == '__main__':
    main()