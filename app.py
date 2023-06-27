#/*Copyright © Eric Cohen 2023*/
#Blackjack game build by Eric Cohen for MSTU5003
#This game is meant to teach me how to use flask better
#Than my previous assignmnet. Hopefully I get the hang of things
#Anyway, have fun!

from flask import Flask, request, url_for, redirect, render_template
from play import play
from player import player
app = Flask(__name__)
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
    #To some degree, I feel like this would go well in a JSON
    renderVars = {
        "hide_name": "",
        "tagline": "Enter your name, soldier",
        "cards": [], #Player cards
        "hands": [], #Dealer cards
        "results_hidden": "hidden", #Hiding of the results. Should be "hidden" or ""
        "result_text": "" #Pretty self_explanatory
    }
    gameHandler = play() #play class for game logic
    #Generates deck when there is none
    #(rests o nother pages)
    playerCards = [gameHandler.deal(deck)]
    dealerCard = gameHandler.deal(deck)
    playerCards.append(gameHandler.deal())
    dealerLaterCard = gameHandler.deal()
    dealer = player("dealer", dealerCard[0], "")
     player("", playerCards[0], playerCards[1])
    #Set player name
    if ('nametag' in request.form):
        player.setName(request.form['user_inpt'])
        #Similar to Java, points to variable instead of assigned
        renderVar["cards"] = dealer.getHand()
        renderVar["hideName"] = "hidden" #Hides the name field by assigning hidden class
        renderVar["hands"] = player.getHand()
    elif ('hit' in request.form and renderVar["hideName"] == "hidden"):
        player.appendHand(gameHandler.deal())
        if (player.sumTotal() == 21):
            renderVars["result_text"] = gameHandler.runDealer(dealer, player)
            renderVars["result_hidden"] = "" #Unhides the results
    elif ('stay' in request.form and renderVar["hideName"] == "hidden"):
        #Going to have the logic go all at once
        #Not going to handle rendering the page for each deal
        dealer.appendHand(dealerLaterCard)
        renderVars["result_text"] = gameHandler.runDealer(dealer, player)
        renderVars["result_hidden"] = "" #Unhides the results
    elif ('split' in request.form and renderVar["hideName"] == "hidden" and len(player.getHand()) == 2
    and player.getHand()[0] == player.getHand()[1]):
        #Not going to implement this
        pass
    #Grab name
    #Re_render with restart button
    return render_template("/play.html", hide_name=renderVars["hide_name"], tagline=renderVars["tagline"],
    cards=renderVars["cards"], hands=renderVars["hands"], results_hidden=renderVars["results_hidden"],
    results_text=renderVars["results_text"])

#404 error errorhandler
#[CYNICAL] hehehe
@app.errorhandler(404)
def page_not_found(e):
    deck = []
    return render_template('404.html'), 404

#Runs the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2424, debug=True)
