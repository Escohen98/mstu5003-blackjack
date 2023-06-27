#Copyright © Eric Cohen 2023
#Player object to store the name, hand, and sum.
class player():

    #Initialize player with name and cards
    #Either 1 or 2 cards depending on player or dealer
    #Throws exception otherwise
    def __init__(self, name, *cards):
        self.name = name #Cannot be changed once set.
        self.hand = []

        if (len(cards) == 0 or len(cards) > 2):
            throw Exception("Only 1 or 2 cards plz. K thx.")

        for (card in cards):
            hand.append(card)

    #Checks the total of the cards
    #Returns the sum, as per blackjack rules.
    def sumTotal():
        sum = 0
        for arg in hand:
            #Handles 11 (ace) going above 21
            if (arg == 16 and sum+arg > 21):
                sum += 1
            elif (arg == 16): #Handles Ace
                sum += 11
            elif (arg >= 10): #Handles royals
                sum += 10
            else:
                sum += arg
        return sum

    #Helper function to get player's name
    def getName():
        return self.name

    #Helper function to set player's name
    #Only works if player's name is blank
    def setName(name):
        if (self.name == None or self.name == ""):
            self.name = name

    #Helper function to get the player's hand
    def getHand():
        return self.hand

    #Helper function to add a new card to the hand
    def appendHand(card):
        self.hand.append(card)
