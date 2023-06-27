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
    def generateDeck(self):
        #Card number
        for i in range(2,17):
            #Number of each card
            for j in range(4):
                self.deck.append(i)
        return self.deck;

    #Takes a deck array, shuffles it
    #Returns and removes the last element of the array
    def deal(self):
        #Cool new function I never knew about
        random.shuffle(self.deck)
        return self.deck.pop()

    #Handles dealer play. Going to be re-used
    def runDealer(self,dealer, player):
        while dealer.sumTotal() < 16:
            dealer.appendHand(self.deal())
        if dealer.sumTotal() > 21 or dealer.sumTotal() > player.sumTotal():
            return "You lose. HAHAHAHAHAHAAHHAHA"
        elif dealer.sumTotal() < player.sumTotal():
            return "It's a draw :/"
