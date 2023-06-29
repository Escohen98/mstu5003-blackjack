#/*Copyright © Eric Cohen 2023*/
#Blackjack game build by Eric Cohen for MSTU5003
#This game is meant to teach me how to use flask better
#Than my previous assignmnet. Hopefully I get the hang of things
#Anyway, have fun!

from flask import Flask, request, url_for, redirect, render_template, session
from play import play
from player import player
app = Flask(__name__)
app.secret_key = 'th1s1s4s3cr3t!'
deck = [] #The deck

#Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    deck = []
    #Blackjack image link.
    #Mostly doing this to play around with if statement.
    image = 'http://cliparts.co/cliparts/Bcg/rbG/BcgrbGk7i.jpg'
    alt = "card_image"
    return render_template('./home.html', image=image, img_alt=alt)


#Play (main) page
@app.route('/play.html', methods=['GET', 'POST'])
def game():
    renderVars = {
        "hide_name": "",
        "tagline": "Enter your name, soldier",
        "cards": [],
        "hands": [],
        "results_hidden": "hidden",
        "result_text": ""
    }
    gameHandler = play()  # create an instance of the play class

    if 'deck' in session:
        gameHandler.deck = session['deck']

        # check the existence of all session keys before accessing them
        if 'dealer_card' in session and 'dealer_hand' in session and 'player_hand' in session and 'player_name' in session and 'cards' in session:
            dealerCard = session['dealer_card']
            dealer = player("dealer", dealerCard, "")
            dealer.setHand(session['dealer_hand'])

            playerCards = session['player_hand']
            playerName = session['player_name']
            user_player = player(playerName, playerCards[0], playerCards[1])

            cards = session['cards']
        else:
            gameHandler.generateDeck()
            session['deck'] = gameHandler.deck  # stores the deck in the session
            cards = []
            for i in range(4):
                cards.append(gameHandler.deal())
            session['cards'] = cards
            #Order of dealing
            playerCards = [cards[0]]
            dealerCard = cards[1]
            playerCards.append(cards[2])
            dealerLaterCard = cards[3]
            dealer = player("dealer", dealerCard, "")
            user_player = player("", playerCards[0], playerCards[1])
            session['dealer_card'] = dealerCard
            session['dealer_hand'] = dealer.getHand()
            session['player_hand'] = playerCards
            session['player_name'] = ""
            session.modified = True

    if 'nametag' in request.form:
        user_input = request.form.get('user-inpt')  # use .get to avoid KeyError
        #handles empty name.
        if user_input:  # Check if the user input is not empty
            user_player.setName(user_input)
            session['player_name'] = user_input
            session.modified = True
        else:
            return "No name was provided", 400  # Handle the case when no name is provided
        renderVars["cards"] = dealer.getHand()
        renderVars["hide_name"] = "hidden"
        renderVars["hands"] = user_player.getHand()
    elif 'hit' in request.form and renderVars["hide_name"] == "hidden":
        player.appendHand(gameHandler.deal())
        session['player_hand'] = user_player.getHand()
        session.modified = True
        if user_player.sumTotal() == 21:
            renderVars["result_text"] = gameHandler.runDealer(dealer, user_player)
            renderVars["results_hidden"] = ""
    elif 'stay' in request.form and renderVars["hide_name"] == "hidden":
        dealer.appendHand(dealerLaterCard)
        session['dealer_hand'] = dealer.getHand()
        session.modified = True
        renderVars["result_text"] = gameHandler.runDealer(dealer, user_player)
        renderVars["results_hidden"] = ""
    elif 'split' in request.form and renderVars["hide_name"] == "hidden" and len(player.getHand()) == 2 and player.getHand()[0] == player.getHand()[1]:
        pass

    return render_template("/play.html", hide_name=renderVars["hide_name"], tagline=renderVars["tagline"],
                           pname=user_player.getName(), cards=gameHandler.royals(renderVars["cards"]), hands=gameHandler.royals(renderVars["hands"]),
                           results_hidden=renderVars["results_hidden"], result_text=renderVars["result_text"])

#Play (main) page
@app.route('/play.html', methods=['GET', 'POST'])
def game():

#404 error errorhandler
#[CYNICAL] hehehe
@app.errorhandler(404)
def page_not_found(e):
    deck = []
    return render_template('404.html'), 404

#Takes in a tertiary value and returns an array.
# 1 for win message.
# -1 for lose message.
# 0 for draw.
def getResults(result):
    if (result == 1):
        return ["Oh noz, you won. Why??? 😱😭😵🤬🤢👿", "[GIF URL]"
    if (result == -1):
        return ["You lose. 😆🤣😂😁╰(*°▽°*)╯😉🤩🥰😘😎😳🥳🫢😛", "[GIF URL]"]

    return ["It's a draw 🫤", "[GIF URL]"]

#Runs the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2424, debug=True)
