import deck
import card
import player
import game
import gameround

class Hand:
    def __init__(self):
        """
        Constructor for a hand of cards
        """
        self.h = []

    def getHand(self) -> list:
        """
        Returns a hand of cards
        """
        return self.h

    def clearHand(self):
        """
        Empties a hand of cards
        """
        self.h = []

    def getCard(self, i: int) -> card:
        """
        Returns a card from a specified index
        ---
        i: index of hand
        """
        return self.h[i]

    def displayHand_WD(self):
        """
        Prints out hand with details
        """
        for i in range(len(self.h)):
            self.h[i].displayCard()

    def displayHand(self):
        """
        Prints out hand with only card index and name
        """
        for i in range(len(self.h)):
            print(str(i) + ": " + self.h[i].getName())
        print()

    def draw(self, d: deck):
        """
        Draws a card from the deck into the hand
        """
        self.h.append(d.draw())

    def countessCheck(self) -> bool:
        """
        Returns True if Countess is in the same hand as a King/Prince
        """
        if len(self.h) < 2:
            return False
        rank0 = self.h[0].getRank()
        rank1 = self.h[1].getRank()
        if rank0 == 7 and (rank1 == 5 or rank1 == 6):
            return True
        elif rank1 == 7 and (rank0 == 5 or rank0 == 6):
            return True
        return False

    def discard(self) -> card:
        """
        Discards and returns card in hand
        """
        return self.h.pop(0)
    
    def playCard(self, i: int, p: player, d: deck, g: game, r: gameround):
        """
        Plays a card from hand
        Calls specific functions depending on what card is played
        ---
        i: index of hand
        p: player that is playing the card
        d: deck being used
        g: game being played
        r: current round
        """
        # if handmaid was in effect from previous turn, it gets turned off
        if p.getHandmaid() == True:
            p.setHandmaid(False)
        
        tmp = self.h.pop(i)
        if tmp.getRank() == 1:
            g.playGuard(p, r)
        elif tmp.getRank() == 2:
            g.playPriest(p, r)
        elif tmp.getRank() == 3:
            g.playBaron(p, r)
        elif tmp.getRank() == 4:
            g.playHandmaid(p, r)
        elif tmp.getRank() == 5:
            g.playPrince(p, d, r)
        elif tmp.getRank() == 6:
            g.playKing(p, r)
        elif tmp.getRank() == 7:
            g.playCountess(p, r)
        elif tmp.getRank() == 8:
            g.playPrincess(p, r)
        
        
            
