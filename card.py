#Represents a single playing card

class Card:
    def __init__(self):
        """
        Constructor for a card
        name of card
        rank of card
        description of card
        """
        self.name = ""
        self.rank = 0
        self.description = ""

    def getName(self) -> str:
        """
        Returns name of card
        """
        return self.name

    def getRank(self) -> int:
        """
        Returns rank of card
        """
        return self.rank

    def getDescription(self) -> str:
        """
        Returns description of card
        """
        return self.description

    def displayCard(self):
        """
        Displays card's details
        """
        print("       Name: ", self.name)
        print("       Rank: ", self.rank)
        print("Description: ", self.description)
        print("")

# specific playing cards
class Princess(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Princess"
        self.rank = 8
        self.description = "If you discard this card, you are out of the round."
    
class Countess(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Countess"
        self.rank = 7
        self.description = "If you have this card and the King or Prince in your hand, you must discard this card."

class King(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "King"
        self.rank = 6
        self.description = "Trade hands with another player of your choice."
    
class Prince(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Prince"
        self.rank = 5
        self.description = "Choose any player (including yourself) to discard his or her hand and draw a new card."    

class Handmaid(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Handmaid"
        self.rank = 4
        self.description = "Until your next turn, ignore all effects from other players' cards."

class Baron(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Baron"
        self.rank = 3
        self.description = "You and another player secretly compare hands. The player with the lower value is out of the round."

class Priest(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Priest"
        self.rank = 2
        self.description = "Look at another player's hand."

class Guard(Card):
    def __init__(self):
        Card.__init__(self)
        self.name = "Guard"
        self.rank = 1
        self.description = "Name a non-Guard card and choose a player. If that player has that card, he or she is out of the round."
