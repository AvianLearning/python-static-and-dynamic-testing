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
    
    def test_can_find_highest_card(self):
        self.assertEqual(self.ten_of_hearts, self.card_game.highest_card(self.ace_of_clubs, self.ten_of_hearts))

    def test_can_find_total_cards(self):
        card_1 = Card("diamonds", 8)
        card_2 = Card("spades", 2)
        card_3 = Card("clubs", 10)
        card_4 = Card("hearts", 9)
        cards = [card_1, card_2, card_3, card_4]
        self.assertEqual("You have a total of 29", self.card_game.cards_total(cards))
