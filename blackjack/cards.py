import random


class Card:
    """Represents the cards in a deck."""
    def __init__(self, suite, kind, value):
        """Initialize attributes to describe a card."""
        self.suite = suite
        self.kind = kind
        self.value = value

    def describe(self):
        """Returns the description of the card."""
        description = [self.suite, self.kind, self.value]
        return description

    # hearts_ace = Card("hearts", "ace", 1)
    # print(type(hearts_ace.describe()))


class Deck:
    """Represents a deck of cards."""
    def __init__(self):
        """Initialize attributes to describe a deck of cards."""
        self.total = 52
        self.suites = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.kinds = [
            'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'
        ]
        ace = [1, 11]
        self.composition = [
                Card('Hearts', 'Ace', ace),
                Card('Hearts', '2', 2),
                Card('Hearts', '3', 3),
                Card('Hearts', '4', 4),
                Card('Hearts', '5', 5),
                Card('Hearts', '6', 6),
                Card('Hearts', '7', 7),
                Card('Hearts', '8', 8),
                Card('Hearts', '9', 9),
                Card('Hearts', '10', 10),
                Card('Hearts', 'Jack', 10),
                Card('Hearts', 'Queen', 10),
                Card('Hearts', 'King', 10),
                Card('Spades', 'Ace', ace),
                Card('Spades', '2', 2),
                Card('Spades', '3', 3),
                Card('Spades', '4', 4),
                Card('Spades', '5', 5),
                Card('Spades', '6', 6),
                Card('Spades', '7', 7),
                Card('Spades', '8', 8),
                Card('Spades', '9', 9),
                Card('Spades', '10', 10),
                Card('Spades', 'Jack', 10),
                Card('Spades', 'Queen', 10),
                Card('Spades', 'King', 10),
                Card('Diamonds', 'Ace', ace),
                Card('Diamonds', '2', 2),
                Card('Diamonds', '3', 3),
                Card('Diamonds', '4', 4),
                Card('Diamonds', '5', 5),
                Card('Diamonds', '6', 6),
                Card('Diamonds', '7', 7),
                Card('Diamonds', '8', 8),
                Card('Diamonds', '9', 9),
                Card('Diamonds', '10', 10),
                Card('Diamonds', 'Jack', 10),
                Card('Diamonds', 'Queen', 10),
                Card('Diamonds', 'King', 10),
                Card('Clubs', 'Ace', ace),
                Card('Clubs', '2', 2),
                Card('Clubs', '3', 3),
                Card('Clubs', '4', 4),
                Card('Clubs', '5', 5),
                Card('Clubs', '6', 6),
                Card('Clubs', '7', 7),
                Card('Clubs', '8', 8),
                Card('Clubs', '9', 9),
                Card('Clubs', '10', 10),
                Card('Clubs', 'Jack', 10),
                Card('Clubs', 'Queen', 10),
                Card('Clubs', 'King', 10)
                ]

    def deal(self, player_cards, n):
        """Simulates dealing the deck of cards.
           'player_cards' is the list of cards that have already been dealt.
            'n' is the number of times cards are dealt.
        """
        i = 0
        while i < n:
            card = random.choice(self.composition).describe()
            while card in player_cards:
                card = random.choice(self.composition).describe()
            player_cards.append(card)
            i += 1
        return player_cards


# deck = Deck()
# player = []
# print(deck.deal(player, 4))
