#Copyright © Eric Cohen 2023
#Player object to store and initialize the name, hand, and sum.
class player():
    # Initialize player with name and cards
    # Either 1 or 2 cards depending on player or dealer
    # Throws exception otherwise
    def __init__(self, name, *cards):
        self.name = name  # Cannot be changed once set.
        self.hand = []

        # Should only be 1 or 2 cards. If not, raise an exception.
        if len(cards) == 0 or len(cards) > 2:
            raise Exception("Only 1 or 2 cards allowed.")

        for card in cards:
            self.hand.append(card)

    #Checks the total of the cards
    #Returns the sum, as per blackjack rules.
    def sumTotal(self):
        sum = 0
        for arg in self.hand:
            #Handles 11 (ace) going above 21
            if (arg == 14 and sum+11 > 21):
                sum += 1
            elif (arg == 14): #Handles Ace
                sum += 11
            elif (arg >= 10): #Handles royals
                sum += 10
            else:
                sum += arg
        return sum

    #Helper function to get player's name
    def getName(self):
        return self.name

    #Helper function to set player's name
    #Only works if player's name is blank
    def setName(self, name):
        self.name = name

    #Helper function to get the player's hand
    def getHand(self):
        return self.hand if self.hand is not None else []

    #Adding to the player's hand
    def setHand(self, hand):
        self.hand = hand

    #Helper function to add a new card to the hand
    def appendHand(self, card):
        self.hand.append(card)
