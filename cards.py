from ranks import Rank
#from suit import Suit
import random

class Card():
    def __init__(self, rank):
        self.rank = rank.value
       # self.suit = suit.value

    def __repr__(self):
        return f"{self.rank}"
    
    @staticmethod
    def new_deck():
        deck = []
        for rank in Rank:
            #for suit in Suit:
            deck.append(Card(rank))
        random.shuffle(deck)
        return deck
    
### Examples

# Making a new card


#card_1 = Card(Rank.ACE, Suit.HEARTS)
#card_2 = Card(Rank.TWO, Suit.DIAMONDS)
#card_3 = Card(Rank.THREE, Suit.CLUBS)
#card_4 = Card(Rank.FOUR, Suit.SPADES)

# Making a new deck
deck = Card.new_deck()
