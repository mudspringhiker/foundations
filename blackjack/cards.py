import random
import itertools


class Card:
    """Represents an individual card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        """Returns the description of the card."""
        return "{} of {}".format(self.rank, self.suit)

    def value(self):
        """Returns the value of the card."""
        if self.rank == 'ACE':
            self.value = 11
        elif self.rank in [str(_) for _ in range(2, 11)]:
            self.value = int(self.rank)
        else:
            self.value = 10
        return self.value

# a_card = Card("hearts", "8")
# print(a_card)
# value = a_card.value()
# print("value: {}".format(value))
# print(type(value))


class Deck:
    """Represents a deck of cards."""
    def __init__(self):
        ranks = [str(__) for __ in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
        suits = ['SPADES', 'HEARTS', 'DIAMONDS', 'CLUBS']
        self.composition = [Card(s, r) for s, r in itertools.product(suits, ranks)]
        random.shuffle(self.composition)

    def deal(self):
        """
        Simulates dealing a card from a deck to a player.
        :returns a list
        """
        return self.composition.pop()


# deck = Deck()
# print(len(deck.composition))
# player_hand = []
# print('player hand: {}'.format(player_hand))
# print("Dealing...")
# player_hand.append(deck.deal())
# print("player_hand = {}".format(player_hand))
# print(len(deck.composition))
# print("Dealing...")
# player_hand.append(deck.deal())
# print("player_hand = {}".format(player_hand))
# print(len(deck.composition))
