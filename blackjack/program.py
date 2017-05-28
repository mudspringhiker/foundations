from cards import Deck


def main():
    """Simulates the game of Blackjack."""
    print_header()
    # deal card (give 2 cards to player after randomizing)
    while True:
        response = input("Are you ready to play?(y/n) ")
        if response == 'y':
            print("Ok, let's begin!")
            deck = Deck()
            player_cards = []
            deal_player(deck, player_cards, 2)
            print(player_cards)
            break
        else:
            print("Ok, exiting...goodbye!")
            break
    # determine sum of 2 cards dealt and assign to a variable
    # if blackjack, player wins, the hand wins
    # ask player "would you like to play another hand
    # if yes - got back to step 3
    # otherwise, quit
    # otherwise proceed to steps below
    # ask player if he/she wants another card
    # if yes give card
    # if no do nothing
    # determine sum of cards
    # if less than 21:
    # ask hit or stand
    # hit - give card
    # go back to "determine sum of cards"
    # stand - do nothing
    # if = 21:
    # player wins, dealer busts
    # if > 21:
    # player busts, dealer wins


def print_header():
    print("---------------------------------")
    print("          Blackjack App")
    print("---------------------------------")
    print()


def deal_player(deck_of_cards, player_cards, n):
    """
    Deals card/cards to player from deck.
    'deck_of_cards' is the instantiated Deck
    'player_cards' is the list of cards the player has (empty if none)
    'n' is the number of times a card will be dealt the player
    """
    i = 0
    while i < n:
        card = deck_of_cards.deal()
        while card in player_cards:
            card = deck_of_cards.deal()
        print("Your card is {}.".format(card))
        player_cards.append(card)
        i += 1
    return player_cards


def game_loop():
    """Asks player if he/she wants to hit or stand."""

    while True:
        cmd = input("Do [h]it or [s]tand? ")
        if cmd == 'h':
            print('h')
        elif cmd == 's':
            print('s')
        else:
            print("Ok, Goodbye!")
            break


if __name__ == "__main__":
    main()
