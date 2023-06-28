#Copyright © Eric Cohen 2023
#Class to handle the playing of Blackjack.
#Keeps app.py from getting too cluttered.
import random

class play():
    deck = []
    #Generates Deck. It's 1d.
    #Suits don't matter.
    #Adds 4 of each 2-16 into an array
    #Returns array
    def generateDeck(self):
        self.deck = []
        for i in range(2, 17):
            for j in range(4):
                self.deck.append(i)
        return self.deck


    #Takes a deck array, shuffles it
    #Returns and removes the last element of the array
    def deal(self):
        #Cool new function I never knew about
        random.shuffle(self.deck)
        return [self.deck.pop()]

    #Handles dealer play. Going to be re-used
    def runDealer(self,dealer, player):
        while dealer.sumTotal() < 16:
            dealer.appendHand(self.deal())
        if dealer.sumTotal() > 21 or dealer.sumTotal() > player.sumTotal():
            return "You lose. 😆🤣😂😁╰(*°▽°*)╯😉🤩🥰😘😎😳🥳🫢😛"
        elif dealer.sumTotal() < player.sumTotal():
            return "Oh noz, you won. Why??? 😱😭😵🤬🤢👿"
        else:
            return "It's a draw 🫤"

    #Converts numbers to royals
    #Returns number if not a royal
    #Needs to be an array b/c it would mess up sumTotal()
    #I could make a convert back, but that just seems extra ¯\_(ツ)_/¯
    def royals(self, cards):
        newCards = []
        for card in cards:
            if card == 11:
                newCards.append('J')
            elif card == 12:
                newCards.append('Q')
            elif card == 13:
                newCards.append('K')
            elif card == 14 or card == 1: #Card should never equal 1, but you never know
                newCards.append('A')
            else:
                return card
