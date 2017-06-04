import time
from cards import Deck, hand_value


def main():
    """
    Simulates the game of blackjack.
    """
    print_header()
    game_loop()


def print_header():
    """
    This method prints out the header for the app. 
    """
    print("---------------------------------")
    print("          BLACKJACK!")
    print("---------------------------------")


def game_loop():

    while True:

        print()
        gameinit = input('Do you want to play?(y/n) ')

        if gameinit != 'n':

            # Initialize deck of cards
            print("Shuffling deck of cards...")
            deck = Deck()
            time.sleep(2)
            print()

            # Initialize player's and dealer's hands
            player_hand = []
            dealer_hand = []

            # Deal 2 cards for player and dealer
            print("Dealing cards:")
            for i in range(2):
                print("Player...")
                player_hand.append(deck.deal())
                print("Dealer...")
                dealer_hand.append(deck.deal())
            print()
            print("Dealer's card: \n\t{}".format(dealer_hand[1]))
            print()

            # Show cards and determine sum of cards
            show(player_hand)
            print()
            player_hand_value = hand_value(player_hand)
            print('The value of your cards is {}.'.format(player_hand_value))

            # Consequence of the sum
            if player_hand_value == 21:
                print("Blackjack, 21! You won!")
            elif player_hand_value > 21:
                print("Bust! You lose!")
            else:
                # Ask player to hit or stand
                cmd = input("Do you [h]it or [s]tand? ")
                print()

                while cmd == 'h':
                    player_hand.append(deck.deal())
                    show(player_hand)
                    player_hand_value = hand_value(player_hand)
                    print('The value of your cards is {}.'.format(player_hand_value))
                    if player_hand_value == 21:
                        print("Blackjack, 21! You won!")
                        break
                    elif player_hand_value > 21:
                        print("Bust! You lose!")
                        break
                    else:
                        cmd = input("Do you [h]it or [s]tand? ")

                dealer_hand_value = hand_value(dealer_hand)
                print('Dealer is at {} with the hand {}.'.format(dealer_hand_value, dealer_hand))
                print('Player is at {} with the hand {}.'.format(player_hand_value, player_hand))
                if (player_hand_value >= dealer_hand_value) and (player_hand_value < 21):
                    print('You won!')
                elif dealer_hand_value == 21:
                    print('You lost!')

        else:
            print("Ok, exiting game...bye!")
            break


def show(player_hand):
    print('Your cards are:')
    for card in player_hand:
        print("\t{}".format(card))


if __name__ == "__main__":
    main()
