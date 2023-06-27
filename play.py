#Copyright © Eric Cohen 2023
#Class to handle the playing of Blackjack.
# Keeps app.py from getting too cluttered.
import random

class play():
    deck = []
    #Generates Deck. It's 1d.
    #Suits don't matter.
    #Adds 4 of each 2-16 into an array
    #Returns array
    def generateDeck():
        #Card number
        for (i=2; i<17; i++):
            #Number of each card
            for (j=0; j<4; j++):
                deck.append(i);
        return deck;

    #Takes a deck array, shuffles it
    #Returns and removes the last element of the array
    def deal(deck):
        #Cool new function I never knew about
        random.shuffle(deck)
        return deck.pop()

    #Handles dealer play. Going to be re-used
    def runDealer(dealer, player):
        while dealer.sumTotal() < 16:
            dealer.appendHand(gameHandler.deal())
        if dealer.sumTotal() > 21 or dealer.sumTotal() > player.sumTotal():
            return = "You lose. HAHAHAHAHAHAAHHAHA"
        elif dealer.sumTotal() < player.sumTotal():
            return = "It's a draw :/"
