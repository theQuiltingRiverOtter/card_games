class Player:
    """Creates a player with a name, hand, and money"""

    def __init__(self, name, money):
        self._name = name
        self._money = money  # not currently being used
        self._hand = []

    def get_name(self):
        return f"{self._name}"

    def get_hand(self):
        return self._hand

    def set_hand(self, hand):
        """Takes a list of cards and puts them in the player's hand"""
        for card in hand:
            self._hand.append(card)
        return self._hand

    def print_hand(self):
        for card in self._hand:
            print(card)
