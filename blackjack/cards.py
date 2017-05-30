import random


class Card:
    """Represents an individual card."""
    def __init__(self, suite, kind, value):
        self.suite = suite
        self.kind = kind
        self.value = value

    def __repr__(self):
        """Returns the description of the card."""
        return "{} of {}".format(self.kind, self.suite)

# hearts_ace = Card("hearts", "king", 10)
# print(hearts_ace)


class Deck:
    """Represents a deck of cards."""
    def __init__(self):
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

    def deal(self, player: list) -> list:
        """
        Simulates dealing the deck of cards to 'player' (a list). 
        :returns a list of cards dealt
        """
        card = random.choice(self.composition)
        self.composition.remove(card)
        player.append(card)
        return player


deck = Deck()
print(len(deck.composition))
player = []
print(deck.deal(player))
print(len(deck.composition))
print()
print(deck.deal(player))
print(len(deck.composition))

print()
print(deck.deal(player))
print(len(deck.composition))