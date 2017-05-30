from cards import Deck


def main():
    """
    Simulates the game of blackjack.
    """
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
    """
    This method prints out the header for the app. 
    """
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
            play()
        elif cmd != 'n':
            print("Sorry, I didn't understand {}.".format(cmd))
        else:
            print("Ok, Goodbye!")


def play():
    """Outlines blackjack game."""
    deck = Deck()
    player_cards = []
    dealer_cards = []
    deck.deal(player_cards, )
    deck.deal(dealer_cards, 1)





if __name__ == "__main__":
    main()
