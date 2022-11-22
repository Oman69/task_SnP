from unittest import TestCase, main
from ..task_06 import rps_game_winner, WrongNumberOfPlayersError, NoSuchStrategyError



class TaskTest(TestCase):
    def test_1(self):
        self.assertEqual(rps_game_winner([['player1', 'P'], ['player2', 'S']]), 'player2 S')

    def test_2(self):
        self.assertRaises(WrongNumberOfPlayersError, rps_game_winner, [['player1', 'P'], ['player2', 'S'], ['player2', 'S']])

    def test_3(self):
        self.assertEqual(rps_game_winner([['player1', 'R'], ['player2', 'P']]), 'player2 P')

    def test_4(self):
        self.assertEqual(rps_game_winner([['player1', 'S'], ['player2', 'R']]), 'player2 R')

    def test_5(self):
        self.assertEqual(rps_game_winner([['player1', 'S'], ['player2', 'S']]), 'player1 S')

    def test_6(self):
        self.assertRaises(NoSuchStrategyError, rps_game_winner, [['player1', 'S'], ['player2', 'K']])

    def test_7(self):
        self.assertRaises(WrongNumberOfPlayersError, rps_game_winner)

if __name__ == '__main__':
    main()