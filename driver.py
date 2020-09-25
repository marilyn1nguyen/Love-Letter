import card
import deck
import hand
import player
import gameround
import game


def main():
    """
    Driver for running Love Letter
    """
    choice = 'y' # choice to start a game
    while choice.lower() == 'y':
        g = game.Game() # initializes a game
        p = g.getPlayers() # list of players
        ptr = 1 # pointer to the player whose turn it is
        roundCounter = 1 # keeps track of the number of rounds
        
        gameInProgress = True 
        while gameInProgress:
            d = deck.Deck() # initialize deck for each round
            r = gameround.Gameround(roundCounter, g, d) # initialize round
            goal = g.maxTokens() # number of tokens to win

            # Indicates start of each round
            input("Press enter to start the round\n")
            g.filler()
            r.startMessage(g)
            g.passMessage(ptr)
            input("Press enter to continue\n")
            
            roundInProgress = True
            while roundInProgress:
                if d.isEmpty(): # check if deck is empty
                    print("The deck is empty! Now comparing the hands of remaining players..")
                    results = r.tieDecider(g)
                    if results == 0: # case of a tie
                        r.tieMessage()
                        roundCounter += 1
                        roundInProgress = False
                        
                    else: # tiebreaker
                        p[results].incTokens()
                        r.winnerMessage(p[results])
                        if p[results].getTokens() == goal:
                            g.winnerMessage(p[results])
                            roundInProgress, gameInProgress = False, False
                            choice = input("Play another game? (Y/N): ")
                        roundCounter += 1
                        roundInProgress = False
                else:
                    # shown on each turn
                    print("Cards left in the deck: " + str(d.cardsLeft()) + "\n")
                    r.displayTrash()
                    r.displayQ()

                    # prompt for user to play a card
                    p[ptr].drawCardPrompt(d)
                    choice = p[ptr].playCardPrompt()
                    p[ptr].getHand().playCard(choice, p[ptr], d, g, r)

                    # checks if the is a winner
                    end = r.endOfRound(d, g)
                    if end == 1: # 1 player left
                        for i in range(1, len(p)):
                            if p[i].getStatus():
                                ptr = i
                        p[ptr].incTokens()
                        r.winnerMessage(p[ptr])
                        roundCounter += 1
                        roundInProgress = False
                        if p[ptr].getTokens() == g.maxTokens():
                            g.winnerMessage(p[ptr])
                            roundInProgress, gameInProgress = False, False
                            choice = input("Play another game? (Y/N): ")
                    elif end == 2: # deck is empty
                        results = r.tieDecider(g)
                        if results == 0: # case of tie
                            r.tieMessage()
                            roundCounter += 1
                            roundInProgress = False
                        else: # tiebreaker
                            p[results].incTokens()
                            r.winnerMessage(p[results])
                            if p[results].getTokens() == goal:
                                g.winnerMessage(p[results])
                                roundInProgress, gameInProgress = False, False
                                choice = input("Play another game? (Y/N): ")
                            roundCounter += 1
                            roundInProgress = False

                    # changes ptr to next player that is still in the round 
                    else:
                        while True:
                            if (ptr + 1) == len(p):
                                ptr = 1
                            else:
                                ptr += 1
                            if p[ptr].getStatus():
                                input("Press enter to end your turn\n")
                                g.filler()
                                g.passMessage(ptr)
                                input("Press enter to continue\n")
                                break
                    
    print("\nGoodbye.")        
        
if __name__ == "__main__":
    main()
