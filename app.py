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
    gameHandler = play() #play class for game logic
    #Generates deck when there is none
    #(rests o nother pages)
    deck = gameHandler.generateDeck()
    player = player(request.form.get('user-inpt'), gameHandler.deal(deck), gameHandler.deal(deck))

    #Grab name
    #Re-render with restart button
    tagline = "Enter your name, soldier"
    return render_template("/play.html", tagline=tagline)

@app.route('/results.html', methods['GET'])
def results():
    return render_template("/results.html")

#404 error errorhandler
#[CYNICAL] hehehe
@app.errorhandler(404)
def page_not_found(e):
    deck = []
    return render_template('404.html'), 404

#Runs the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2424, debug=True)
