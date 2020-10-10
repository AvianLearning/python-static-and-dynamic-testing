import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    def setUp(self):
        self.ace_of_clubs = Card("clubs", 1)
        self.ten_of_hearts = Card("hearts", 10)
        self.card_game = CardGame()

    def test_can_find_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.ace_of_clubs))

        
