from deck import Deck
from player import Player


def get_points(hand):
    """Passes in a list of cards and calculates the points they are worth"""
    face_cards = "JQK"
    total_points = 0
    for card in hand:
        if card.value == "A":
            total_points += 11
        elif card.value in face_cards:
            total_points += 10
        else:
            total_points += int(card.value)
    if total_points > 21:
        for card in hand:
            if card.value == "A":
                total_points -= 10
    return total_points


def winner(p1, p2):
    """Takes in two Player objects and prints who is the winner"""
    p1_points = get_points(p1.get_hand())
    p2_points = get_points(p2.get_hand())
    print(f"{p1.get_name()}: {p1_points}   {p2.get_name()}: {p2_points}")
    if p1_points > 21 or p2_points == 21:
        print(f"{p2.get_name()} wins")
    elif p1_points == 21 or p2_points > 21:
        print(f"{p1.get_name()} wins")
    elif p1_points == p2_points:
        print(f"You both tied")
    elif p1_points < p2_points:
        print(f"{p2.get_name()} wins")
    else:
        print(f"{p1.get_name()} wins")


def blackjack():
    """Runs the blackjack game"""
    playerContinue = True
    computerContinue = True

    # Make and shuffle the deck
    deck = Deck.make_standard_deck()
    deck.shuffle()

    # create players
    player = Player("player", 500)
    computer = Player("computer", 500)

    # deals 2 cards out to each player
    player.set_hand(deck.deal_hand(2))
    computer.set_hand(deck.deal_hand(2))

    player.print_hand()
    # runs a loop for both the player and computer to determine if they should hit
    while playerContinue or computerContinue:
        c_points = get_points(computer.get_hand())
        p_points = get_points(player.get_hand())
        if c_points >= 21 or p_points >= 21:
            break
        # computer loop to decide if to hit
        while computerContinue:
            if c_points < 15:
                computer.set_hand(deck.deal_card())
                break
            else:
                computerContinue = False
                break
        # player loop to decide if to hit
        while playerContinue:
            hit = input("hit? (y/n) ")
            if hit == "y":
                player.set_hand(deck.deal_card())
                player.print_hand()
                break
            elif hit == "n":
                playerContinue = False
                break
            else:
                print("not a valid input")
                continue
    winner(player, computer)


if __name__ == "__main__":
    play = True

    # loop to play blackjack as long as user wants
    while play:
        blackjack()
        playAgain = input("play again (y/n) ")
        if playAgain.lower() == "n" or playAgain == "no":
            play = False
            break
