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

    gameinit = input('Do you want to play?(y/n) ')

    if gameinit == 'y':
        print("Initializing deck of cards...")
        print()
        deck = Deck()
        player_hand = []
        dealer_hand = []
        print("Dealing cards:")
        for i in range(2):
            print("Player...")
            player_hand.append(deck.deal())
            print("Dealer...")
            dealer_hand.append(deck.deal())
        print('Your cards are:')
        for card in player_hand:
            print("\t{}".format(card))
    else:
        print("Exiting game...")


        # sumcards = player[0].value + player[1].value
        # print(sumcards)
        # if sumcards == 21:
        #     print("You won!")
        # else:
        #     cmd = None
        #     while cmd != 'n':
        #         cmd = input("Do you [h]it or [s]tand? ")
        #         cmd = cmd.lower().strip()
        #         if cmd == 'h':
        #             deck.deal(player)
        #             print('Your cards:')
        #             for card in player:
        #                 print(card)
        #
        #         elif cmd != 's':
        #             pass
        #         else:
        #             print("I didn't understand.")
        #             continue


if __name__ == "__main__":
    main()
