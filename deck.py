from card import Card
from random import shuffle


class Deck:
    """Make a deck of cards returned as a list"""

    @classmethod
    def make_standard_deck(cls):
        """Uses class method to make a 52 card standard playing card deck"""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cards = []
        for suit in suits:
            for val in values:
                cards.append(Card(suit, val))
        return cls(cards)

    def __init__(self, cards):
        self._cards = cards

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self._cards)

    def _deal(self, size=1):
        """Removes amount of cards equal to size or what is left in the deck
        and appends them to a list which is returned"""
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt")
        if count < size:
            size = count
        hand = self._cards[-size:]
        self._cards = self._cards[:-size]
        return hand

    def shuffle(self):
        """shuffles the deck of cards if it is a full deck"""
        if self.count() < 52:  # magic number, will be taken out in future code
            raise ValueError("Only full decks can be shuffled")
        shuffle(self._cards)

    def deal_card(self):
        """Call _deal with one card"""
        return self._deal()

    def deal_hand(self, size=5):
        """Call _deal with a specified amount of cards"""
        return self._deal(size)
