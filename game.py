import gameround
import deck
import player

class OOBError(Exception):
    """
    Error for when the selection is out of bounds
    """
    pass

class PlayerOutError(Exception):
    """
    Error for when the selection is an invalid player
    """
    pass

class ThatsYouError(Exception):
    """
    Error for when the player chooses to play themselves
    """
    pass

class Game:
    def __init__(self):
        """
        Constructor for a game
        Takes in number of players, plus their names
        Makes a list containing all the players
        """
        self.welcomeMessage()
        while True:
            try:
                # prompt user to enter number of players
                i = int(input("Enter the number of the players (2-4): "))
                if i < 2 or i > 4:
                    raise OOBError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
        
        self.players = [""] # index 0 is unused
        print()

        # initialize player objects according to user input
        # prompts user to enter names (if empty, use default Player names)
        p1 = player.Player()
        p1Name = input("Enter Player 1's name: ")
        p1Name.strip()
        if p1Name == "":
            p1.setName("Player 1")
        else:
            p1.setName(p1Name)
        self.players.append(p1)

        p2 = player.Player()
        p2Name = input("Enter Player 2's name: ")
        p2Name.strip()
        if p2Name == "":
            p2.setName("Player 2")
        else:
            p2.setName(p2Name)
        self.players.append(p2)

        if i > 2:
            p3 = player.Player()
            p3Name = input("Enter Player 3's name: ")
            p3Name.strip()
            if p3Name == "":
                p3.setName("Player 3")
            else:
                p3.setName(p3Name)
            self.players.append(p3)

        if i == 4:
            p4 = player.Player()
            p4Name = input("Enter Player 4's name: ")
            p4Name.strip()
            if p4Name == "":
                p4.setName("Player 4")
            else:
                p4.setName(p4Name)
            self.players.append(p4)

    def getPlayers(self) -> list:
        """
        Returns the list of players
        """
        return self.players

    def displayPlayers(self):
        """
        Prints the list of players
        Indicates if players are out of the round
        """
        print("List of players")
        for i in range(1, len(self.players)):
            if self.players[i].getStatus() == True:
                print(str(i) + ": " + self.players[i].getName())
            else:
                print(str(i) + ": " + self.players[i].getName() + " (out)")
        print()

    def welcomeMessage(self):
        """
        Welcome message
        Displays rules and card details
        """
        print("~*~WELCOME TO LOVE LETTER!~*~\n")
        print("Love Letter is a strict card game of bluffing, deduction, luck and player elimination.")
        print("Each player is a suitor trying to court the lovely Princess Annette who locked herself in her palace.")
        print("The goal of the game is to write a love letter and to get it delivered first to her.\n")
        print("All players has each two cards in their hands (from a deck of 16, numbered 1-8) and must choose each turn which to play. ")
        print("Powerful cards can lead to early gains, but make you a target for others.\n")
        print("A player wins a round by being the last man standing or by having the highest card at the end.")
        print("The winner of the round receives a token of affection.")
        print("Depending on the number of players, 4-7 tokens are required to be the winner of this game.\n")
        print("Below are the card descriptions\n")
        fmt = '{:12} {:6} {:6} {:105}'
        print(fmt.format('CARD', 'QTY', 'RANK', 'DESCRIPTION'))
        print(fmt.format('Princess', '1', '8', "If you discard this card, you are out of the round."))
        print(fmt.format('Countess', '1', '7', "If you have this card and the King or Prince in your hand, you must discard this card."))
        print(fmt.format('King', '1', '6', "Trade hands with another player of your choice."))
        print(fmt.format('Prince', '2', '5', "Choose any player (including yourself) to discard his or her hand and draw a new card."    ))
        print(fmt.format('Handmaid', '2', '4', "Until your next turn, ignore all effects from other players' cards."))
        print(fmt.format('Baron', '2', '3', "You and another player secretly compare hands. The player with the lower value is out of the round."))
        print(fmt.format('Priest', '2', '2', "Look at another player's hand."))
        print(fmt.format('Guard', '5', '1', "Name a non-Guard card and choose a player. If that player has that card, he or she is out of the round."))
        print()
        
    def filler(self):
        """
        Filler message to prevent players from seeing each other's hands
        """
        print("´´´´¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶\n´´¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶¶¶¶¶¶\n´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶¶¶\n\
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´¶¶¶¶\n¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´¶¶¶¶¶\n¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ ´¶¶¶¶¶´\n\
´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶\n´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶\n´´´´´´´´´¶¶¶¶¶¶¶¶\n´´´´´´´´´´´¶¶¶¶\n\n"*10)


    def maxTokens(self) -> int:
        """
        Returns number of tokens to win
        2 player game = 7 tokens
        3 player game = 5 tokens
        4 player game = 4 tokens
        """
        p = len(self.players)-1
        if p == 2:
            goal = 7
        elif p == 3:
            goal = 5
        else:
            goal = 4
        return goal

    def currentStandings(self):
        """
        Prints list of players and how many tokens they have
        """
        print("Here are the current standings")
        for i in range(1, len(self.players)):
            print(self.players[i].getName() + ": " + str(self.players[i].getTokens()))
        goal = self.maxTokens()
        print("\nYou are playing to " + str(goal) + " tokens.\n")

    def passMessage(self, i: int):
        """
        Prints prompt to pass to the next player
        """
        p = self.players[i].getName()
        print("It is now " + p + "'s turn. Please pass the computer to " + p)

    def playGuard(self, p: player, r: gameround):
        """
        Function for playing a guard card
        """
        r.addTrash("Guard") # add card being played to trash
        self.displayPlayers() # displays players that are in the round
        
        # prompts user to pick a player to target
        while True:
            try:
                target = int(input("Enter the number of the player you wish to guess: "))
                if target < 1 or target >= len(self.players):
                    raise OOBError
                if self.players[target].getStatus() == False:
                    raise PlayerOutError
                if self.players[target] == p:
                    raise ThatsYouError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
            except PlayerOutError:
                print("Oops! That player is already out. Try again.\n")
            except ThatsYouError:
                print("Oops! Don't choose yourself! Try again.\n")
        print()

        # shows user trash pile and list of guessing options
        r.displayTrash()
        print("Guessing options\n8: Princess(1)\n7: Countess(1)\n6: King(1)\n5: Prince(2)\n4: Handmaid(2)\n3: Baron(2)\n2: Priest(2)")

        # prompts user to submit a guess
        while True:
            try:
                guess = int(input("\nEnter the number of the card you wish to guess: "))
                if guess < 2 or guess > 8:
                    raise OOBError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
        print()

        # adds to the queue of moves played and displays actions to user
        mes = p.getName() + " played a Guard against " + self.players[target].getName() + ". "
        # Handmaid nulls card effect
        if self.players[target].getHandmaid() == True: 
            print("Due to the handmaid nothing happens.\n")
            mes += "Due to the handmaid nothing happened."
        else:
            # correct guess -> target knocked out
            if self.players[target].getHand().getCard(0).getRank() == guess: 
                print("You guessed correctly! " + self.players[target].getName() + " is out of the round.\n")
                r.addTrash(self.players[target].getHand().getCard(0).getName())
                self.players[target].setStatus(False)
                mes += (self.players[target].getName() + " is out of the round.")
            # incorrect guess -> nothing happens
            else:
                print("Sorry wrong guess. Better luck next time.\n")
                mes += "Nothing happened."
        r.addQ(mes)

    def playPriest(self, p: player, r: gameround):
        """
        Function for playing a priest card
        """
        r.addTrash("Priest") # add card being played to trash
        self.displayPlayers() # displays players that are in the round

        # prompt user to pick a player to target
        while True:
            try:
                target = int(input("Enter the number of the player you wish to see: "))
                if target < 1 or target >= len(self.players):
                    raise OOBError
                if self.players[target].getStatus() == False:
                    raise PlayerOutError
                if self.players[target] == p:
                    raise ThatsYouError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
            except PlayerOutError:
                print("Oops! That player is already out. Try again.\n")
            except ThatsYouError:
                print("Oops! Don't choose yourself! Try again.\n")
        print()

        # adds to the queue of moves played and displays actions to user
        mes = p.getName() + " played a Priest to look at " + self.players[target].getName() + "'s hand. "
        # Handmaid nulls card effect
        if self.players[target].getHandmaid() == True:
            print("Due to the handmaid nothing happens.\n")
            mes += "Due to their handmaid nothing happened."
        # shows player what is in their target's hand
        else:      
            print(self.players[target].getName() + " is holding a " \
                  + self.players[target].getHand().getCard(0).getName() + ".")
        r.addQ(mes)

    def playBaron(self, p: player, r: gameround):
        """
        Function for playing a baron card
        """
        r.addTrash("Baron") # add card being played to trash
        self.displayPlayers() # displays players that are in the round

        # prompt user to pick a player to target
        while True:
            try:
                target = int(input("Enter the number of the player you wish to compare your hand to: "))
                if target < 1 or target >= len(self.players):
                    raise OOBError
                if self.players[target].getStatus() == False:
                    raise PlayerOutError
                if self.players[target] == p:
                    raise ThatsYouError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
            except PlayerOutError:
                print("Oops! That player is already out. Try again.\n")
            except ThatsYouError:
                print("Oops! Don't choose yourself! Try again.\n")
        print()

        # adds to the queue of moves played and displays actions to user
        mes = p.getName() + " played a Baron against " + self.players[target].getName() + ". "
        # Handmaid nulls card effect
        if self.players[target].getHandmaid() == True:
            print("Due to the handmaid nothing happens.\n")
            mes += "Due to their handmaid nothing happened."
        else:
            mycard = p.getHand().getCard(0)
            oppcard = self.players[target].getHand().getCard(0)
            # card is higher than opponents -> opponent is out
            if mycard.getRank() > oppcard.getRank():
                r.addTrash(oppcard.getName())
                self.players[target].setStatus(False)
                print("Success! Your " + mycard.getName() + " is higher than your opponent's " + oppcard.getName() + ". " + self.players[target].getName() + " is out of the round.\n")
                mes += (self.players[target].getName() + " is out of the round. ")
            # card is lower than opponents -> opponent wins
            elif mycard.getRank() < oppcard.getRank():
                r.addTrash(mycard.getName())
                p.setStatus(False)
                print("Oof! Your " + mycard.getName() + " is lower than your opponent's " + oppcard.getName() + ". You're out of the round.\n")
                mes += (p.getName() + " is out of the round. ")
            # cards are equal -> nothing happens
            else:
                print("Looks like you've got the same card! Nothing happens.\n")
                mes += "Nothing happened."
        r.addQ(mes)

    def playHandmaid(self, p: player, r: gameround):
        """
        Function for playing a handmaid card
        """
        r.addTrash("Handmaid") # add card being played to trash
        p.setHandmaid(True) # enacts handmaid effect
        # adds to the queue of moves played and displays actions to user
        print("You have played the handmaid. You are immune to card effects until your next turn.\n")
        mes = p.getName() + " played a Handmaid. They are immune to card effects until their next turn."
        r.addQ(mes)

    def playPrince(self, p: player, d: deck, r: gameround):
        """
        Function for playing a prince card
        """
        r.addTrash("Prince") # add card being played to trash
        self.displayPlayers() # displays players that are in the round

        # prompt user to pick a player to target
        while True:
            try:
                target = int(input("Enter the number of the player to discard their hand: "))  
                if target < 1 or target >= len(self.players):
                    raise OOBError
                if self.players[target].getStatus() == False:
                    raise PlayerOutError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
            except PlayerOutError:
                print("Oops! That player is already out. Try again.\n")
        print()

        # adds to the queue of moves played and displays actions to user
        mes = p.getName() + " played a Prince against " + self.players[target].getName() + "."
        # Handmaid nulls card effect
        if self.players[target].getHandmaid() == True:
            print("Due to the handmaid nothing happens.\n")
            mes += "Due to their handmaid nothing happened."
        else:
            discarded = self.players[target].getHand().discard()
            r.addTrash(discarded.getName())
            # if opponent holding princess -> opponent is out
            if discarded.getRank() == 8:
                self.players[target].setStatus(False)
                print(self.players[target].getName() + " was holding the Princess! " +\
                      self.players[target].getName() + " is out of the round.\n")
                mes += (self.players[target].getName() + " is out of the round.")
            # if deck is empty -> opponent is out
            elif d.isEmpty():
                self.players[target].setStatus(False)
                print("The deck is empty. " + self.players[target].getName() + " couldn't draw a new card. " +\
                      self.players[target].getName() + " is out of the round.\n")
                mes += (self.players[target].getName() + " is out of the round.")
            # opponent draws new hand
            else:
                self.players[target].getHand().draw(d)
                print(self.players[target].getName() + " discarded their hand and drew a new card.\n")
        r.addQ(mes)

    def playKing(self, p: player, r: gameround):
        """
        Function for playing a king card
        """
        r.addTrash("King") # add card being played to trash
        self.displayPlayers() # displays players that are in the round

        # prompt user to pick a player to target
        while True:
            try:
                target = int(input("Enter the number of the player you wish to trade hands with: "))
                if target < 1 or target >= len(self.players):
                    raise OOBError
                if self.players[target].getStatus() == False:
                    raise PlayerOutError
                if self.players[target] == p:
                    raise ThatsYouError
                break
            except ValueError:
                print("Oops! That wasn't a valid number. Try again.\n")
            except OOBError:
                print("Oops! The number is out of bounds. Try again.\n")
            except PlayerOutError:
                print("Oops! That player is already out. Try again.\n")
            except ThatsYouError:
                print("Oops! Don't choose yourself! Try again.\n")
        print()

        # adds to the queue of moves played and displays actions to user
        mes = p.getName() + " played the King against " + self.players[target].getName() + ". "
        # Handmaid nulls card effect
        if self.players[target].getHandmaid() == True:
            print("Due to the handmaid nothing happens.\n")
            mes += "Due to their handmaid nothing happened."
        #swap hands
        else:
            p1hand = p.getHand()
            p2hand = self.players[target].getHand()
            p.setHand(p2hand)
            self.players[target].setHand(p1hand)
            print("You swapped your " + p1hand.getCard(0).getName() + " for " +\
                  self.players[target].getName() + "'s " + p2hand.getCard(0).getName() + ".\n")
            mes += "They swapped hands."
        r.addQ(mes)

    def playCountess(self, p: player, r: gameround):
        """
        Function for playing a countess card
        """
        r.addTrash("Countess") # add card being played to trash
        # adds to the queue of moves played and displays actions to user
        print("You played the Countess.\n")
        mes = p.getName() + " played the Countess."
        r.addQ(mes)

    def playPrincess(self, p: player,  r: gameround):
        """
        Function for playing a princess card
        """
        r.addTrash("Princess") # add card being played to trash
        p.setStatus(False) # player is out of the game if the princess is played
        
        # adds to the queue of moves played and displays actions to user
        print("You played the Princess. You are out of the round.\n")
        mes = p.getName() + " played the Princess." + p.getName() + " is out of the round."
        r.addQ(mes)
        
    def winnerMessage(self, p: player):
        """
        Prints message announcing the winner of the game
        """
        print(p.getName() + " delivered all their love letters to the princess! They won the game :)\n")

    
            
    
        
    
        

    
        
