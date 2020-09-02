import random
import card

class Deck:
    def __init__(self):
        """
        Constructor for a deck of Love Letter cards
        Shuffles deck
        """
        self.deck = []
        self.deck.append(card.Princess())
        self.deck.append(card.Countess())
        self.deck.append(card.King())
        for i in range(2):
            self.deck.append(card.Prince())
            self.deck.append(card.Handmaid())
            self.deck.append(card.Baron())
            self.deck.append(card.Priest())
        for i in range(5):
            self.deck.append(card.Guard())
        random.shuffle(self.deck)

    def displayDeck(self):
        """
        Displays deck
        """
        for i in range(len(self.deck)):
            self.deck[i].displayCard()

    def isEmpty(self) -> bool:
        """
        Returns true if deck is empty
        """
        if self.deck:
            return False
        return True

    def cardsLeft(self) -> int:
        """
        Returns size of deck
        """
        return len(self.deck)
    
    def draw(self) -> card:
        """
        Draws off top of deck
        """
        return self.deck.pop(0)


