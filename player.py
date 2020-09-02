import deck
import card
import hand
import gameround

class CountessError(Exception):
    """
    Error for when a king/prince is being played instead of the countess
    This is an illegal move
    """
    pass

class OOBError(Exception):
    """
    Error for when the selection is out of bounds
    """
    pass

class Player:
    def __init__(self):
        """
        Constructor for a player object
        """
        self.name = "" # Name of player
        self.tokens = 0 # Tokens won
        self.h = hand.Hand() # Initializes hand
        self.handmaid = False # Handmaid effect is False until the Handmaid card is played
        self.playing = True # True if player is in the round

    def setName(self, n: str):
        """
        Sets player's name
        ---
        n: name
        """
        self.name = n

    def getName(self) -> str:
        """
        Gets player's name
        """
        return self.name

    def incTokens(self):
        """
        Increments player's tokens by 1 if they win the round
        """
        self.tokens += 1
        
    def getTokens(self) -> int:
        """
        Gets player's tokens
        """
        return self.tokens

    def setHand(self, hh: hand):
        """
        Sets player's hand
        ---
        hh: hand to be changed to
        """
        self.h = hh

    def getHand(self) -> hand:
        """
        Gets player's hand
        """
        return self.h

    def setHandmaid(self, b: bool):
        """
        Sets player's handmaid status
        True if handmaid card is in effect
        """
        self.handmaid = b

    def getHandmaid(self) -> bool:
        """
        Gets player's handmaid status
        True if handmaid card is in effect
        """
        return self.handmaid

    def setStatus(self, b: bool):
        """
        Sets player's playing status
        True if player is in the round
        False if player is out
        """
        self.playing = b

    def getStatus(self) -> bool:
        """
        Sets player's playing status
        True if player is in the round
        False if player is out
        """
        return self.playing

    def displayHand_WD(self):
        """
        Displays cards in player's hand with detail
        """
        print(self.name + "'s Hand: ")
        self.h.displayHand_WD()

    def drawCardPrompt(self, d: deck):
        """
        Prompts user to draw a card from the deck into their hand
        """
        x = input("Press enter to draw a card ")
        self.draw(d)

    def draw(self, d: deck):
        """
        Draw a card from the deck into player's hand
        """
        self.getHand().draw(d)
        print("\nYou drew a " + self.h.getCard(1).getName() + "!")
        print()
        self.displayHand_WD()
        print()
        
    def playCardPrompt(self) -> int:
        """
        Prompts user to choose a card to play
        Returns index of card to be played
        """
        print("Your current hand")
        self.h.displayHand()
        while True:
            try:
                ret = int(input("Enter the number of card to play: "))
                if ret != 0 and ret != 1:
                    raise OOBError
                if self.h.countessCheck() == True and self.h.getCard(ret).getRank() != 7:
                    raise CountessError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
            except CountessError:
                print("Oops! You must discard the Countess! Try again.\n")
        print()
        return ret

            
                
        
