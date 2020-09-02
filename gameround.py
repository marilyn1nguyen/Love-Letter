import deck
import card
import player
import game

class Gameround:
    def __init__(self, i: int, g: game, d: deck):
        """
        Constructor for a round within a game
        ---
        i: number of the round
        g: game being played
        d: deck being used
        ---
        Clears players' hands and sets their playing status to True
        Contains trash pile as a dictionary
        Contains a log of moves played as a list/queue
        """
        self.roundNum = i
        self.trash = {'Princess': 0, 'Countess': 0, 'King': 0, 'Prince': 0,\
                      'Handmaid': 0, 'Baron': 0, 'Priest': 0, 'Guard': 0}
        self.q = []
        p = g.getPlayers()
        for i in range(1, len(p)):
            p[i].getHand().clearHand()
            p[i].setStatus(True)
            p[i].getHand().draw(d)
        print()
                  
    def startMessage(self, g: game):
        """
        Prints message to announce beginning of round
        Prints current standings
        """
        print("NOW STARTING ROUND " + str(self.roundNum) + "\n")
        g.currentStandings()
        
    def displayTrash(self):
        """
        Prints all the cards in the trash pile
        """
        print("List of discarded cards")
        for item in self.trash:
            print(item + ": " + str(self.trash[item]))
        print()

    def addTrash(self, s: str):
        """
        Adds card to trash pile
        ---
        s: name of card to be added to trash
        """
        self.trash[s] += 1

    def addQ(self, s: str):
        """
        Adds a move to the queue log
        ---
        s: detailed description of player's move
        """
        if len(self.q) == 4:
            self.q.pop(-1)
        self.q.insert(0, s)

    def displayQ(self):
        if len(self.q) == 0:
            return
        print("These are the last 4 turns made")
        for i in range(len(self.q)):
            print(str(i+1) + ". " + self.q[i])
        for j in range(i+2, 5):
            print(str(j) + ".")
        print()

    def tieDecider(self, g: game) -> int:
        """
        Decides the winner in the case the deck is empty
        ---
        g: game being played
        ---
        Returns 0 if it is a tie and no one wins
        Returns the index of the player corresponding to the list of players
        i.e. if return 1, that means player 1 won
        """
        p = g.getPlayers()
        highestCard = 0
        winner = 0
        tie = True
        for i in range(1, len(p)):
            if p[i].getStatus() == True:
                if p[i].getHand().getCard(0).getRank() > highestCard:
                    if highestCard != 0:
                        tie = False
                    highestCard = p[i].getHand().getCard(0).getRank()
                    winner = i
                elif p[i].getHand().getCard(0).getRank() < highestCard:
                    tie = False
        if tie == True:
            return 0
        return winner     
                
    def endOfRound(self, d: deck, g: game) -> int:
        """
        Checks if the round is over (one player left or deck is empty)
        ---
        d: deck being used
        g: game being played
        ---
        Returns 0 if round is not over
        Returns 1 if one player left
        Returns 2 if deck is empty
        """
        counter = 0
        p = g.getPlayers()
        for i in range(1, len(p)):
            if p[i].getStatus() == True:
                counter += 1
            if counter > 1:
               return 0
        if counter == 1:
            return 1
        elif d.isEmpty():
            return 2

    def tieMessage(self):
        """
        Prints a message in the case of a tie
        """
        print("There was a tie! No one won this round.. starting next round.\n")

    def winnerMessage(self, p: player):
        """
        Prints out message to announce winner of round
        """
        print(p.getName() + " won this round. They now have " + str(p.getTokens()) + " tokens.\n")
        
                
