import random
import itertools


class Card:
    """Represents an individual card."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank == 'ACE':
            self.value = 11
        elif rank in [str(_) for _ in range(2, 11)]:
            self.value = int(rank)
        else:
            self.value = 10

    def __repr__(self):
        """Returns the description of the card."""
        return "{} of {}".format(self.rank, self.suit)


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


def hand_value(hand):
    """Shows player_hand and calculates the value of cards (should be a list)."""
    total = sum(card.value for card in hand)
    num_aces = len([card.rank for card in hand if card.rank == 'ACE'])
    if total > 21 and num_aces > 0:
        while num_aces > 0:
            total -= 10
            num_aces -= 1
    return total
