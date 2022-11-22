from unittest import TestCase, main
from ..task_05 import date_in_future
from datetime import datetime, timedelta


class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(date_in_future(2), (datetime.today() + timedelta(days=2)).strftime('%d-%m-%Y %H:%M:%S'))

    def test_2(self):
        self.assertEqual(date_in_future([]), datetime.today().strftime('%d-%m-%Y %H:%M:%S'))

    def test_3(self):
        self.assertEqual(date_in_future(7), (datetime.today() + timedelta(days=7)).strftime('%d-%m-%Y %H:%M:%S'))

    def test_4(self):
        self.assertEqual(date_in_future(), datetime.today().strftime('%d-%m-%Y %H:%M:%S'))

    def test_5(self):
        self.assertEqual(date_in_future('3 дня'), datetime.today().strftime('%d-%m-%Y %H:%M:%S'))

    def test_6(self):
        self.assertEqual(date_in_future(3.5), datetime.today().strftime('%d-%m-%Y %H:%M:%S'))