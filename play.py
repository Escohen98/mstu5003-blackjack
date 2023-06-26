#Copyright © Eric Cohen 2023
#Class to handle the playing of Blackjack.
# Keeps app.py from getting too cluttered.
class play():

    #Generates Deck. It's 1d.
    #Suits don't matter.
    #Adds 4 of each 2-16 into an array
    #Returns array
    def generateDeck():
        deck = []
        #Card number
        for (i=2; i<17; i++):
            #Number of each card
            for(j=0; j<4; j++):
                deck.append(i);
        return deck;
                 
