#Blackjack game build by Eric Cohen for MSTU5003
#This game is meant to teach me how to use flask better
#Than my previous assignmnet. Hopefully I get the hang of things
#Anyway, have fun!

from flask import Flask, request, url_for, redirect, render_template
app = Flask(__name__)

#Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    #Blackjack image link.
    #Mostly doing this to play around with if statement.
    image = 'http://cliparts.co/cliparts/Bcg/rbG/BcgrbGk7i.jpg'
    alt = "card_image"
    return render_template('./home.html', image=image, img_alt=alt)

#Play (main) page
@app.route('/play.html', methods=['GET', 'POST']):
    return render_template("/play.html")

#404 error errorhandler
#[CYNICAL] hehehe
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#Runs the server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2424, debug=True)
