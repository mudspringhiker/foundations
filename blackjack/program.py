from cards import Deck


def main():
    """Simulates the game of Blackjack."""
    print_header()
    game_loop()
    # deal card (give 2 cards to player after randomizing)
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


def game_loop():
    """Asks player if he/she wants to hit or stand."""
    print('Do you want to play?')
    cmd = None
    while cmd != 'n':
        cmd = input("[Y]es, [N]o: ")
        cmd = cmd.lower().strip()
        if cmd == 'y':
            print('y')
        elif cmd != 'n':
            print("Sorry, I didn't understand {}.".format(cmd))
        else:
            print("Ok, Goodbye!")


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




if __name__ == "__main__":
    main()
