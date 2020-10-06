import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)
    def test_is_valid(self):
        new_game = Game()
        new_game.grid=list('YDFISELNA')
        self.assertIs(new_game.is_valid(''), False)
        self.assertIs(new_game.is_valid("FINE"),True)
        self.assertEqual(new_game.grid, list('YDFISELNA'))
    def test_is_valid_lower(self):
        new_game = Game()
        new_game.grid=list('YDFISELNA')
        self.assertIs(new_game.is_valid("Finesse"),True)
        self.assertEqual(new_game.grid, list('YDFISELNA'))
    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('FUNE'), False)