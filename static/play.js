//Script used to handle the blackjack game in play.html
//Rewriting code from Python. Yay 😓
let dealer = {
  name: "dealer",
  cards: [],
  total: 0

};

let player = {
  name: "",
  cards: [],
  total: 0
};

(function() {
  window.addEventListener("load", initialize);
  let deck = [];
  let dealLaterCard = -1; //For later

  //Starts loading page with just a name field.
  function initialize() {
    let person = prompt("Enter your name, soldier")
    while(true) {
      if (person == null || person.length < 4) {
        alert()
      }
    }

    let hit = document.getElementById("hit");
    let stay = document.getElementById("stay");
    //Not implementing
    let split = document.getElementById("split");
    document.querySelector("Go!").addEventListener("click", startGame);
    hit.addEventListener("click", hit());
    stay.addEventListener("click", stay());

  }


  /** Game handler **/

  //Runs the game.
  function startGame() {
     if (nameCheck()) { //Makes sure the username has been set.
       break;
     }
    document.getElementById("game-board").classlist.remove("hidden");
    deck = generateDeck();

    //Order of dealing.
    hit(); //Adds to player
    dealer.cards.push(deal());
    hit();


    dealerLaterCard = deal(); //For later.
  }

  //Adds a card to the player's hand.
  //Checks for bust / blackjack & sends to results
  function hit() {
    let total = addCard(player);
    if(total > 21) {
      getResults(-1);
    } else if(total == 21 && player.cards.length == 2) {
      getResults(1);
    }
  }

  //Handles the stay button event.
  function stay() {
    //It's later.
    dealer.cards.push(dealLaterCard);
    getResults(runDealer);
  }

  //Handles dealer logic
  //Returns final result.
  function runDealer(dealer, player) {
    dealer.total = sumTotal(dealer.cards);
    while (dealer.total < 16) {
      dealer.total = sumTotal(dealer.cards);
    }
    return compareTo(player.total, dealer.total);
  }

  /*
   * Handles the results event.
   * Modifies the result paragraph & img elements in #results
   * Checkes if it's a win / loss / tie
   * Also makes the #results section visible while hiding game action buttons.
   */
  function getResults(result) {
    let resultText = document.getElementById("result-msg");
    let resultGif = document.getElementById("result-gif");
    if (result == -1) {
      resultText.innerHTML = "You lose. 😆🤣😂😁╰(*°▽°*)╯😉🤩🥰😘😎😳🥳🫢😛";
      resultGif.src = "https://i.giphy.com/media/OHrZoTiRXq2A/giphy.webp";
    } else if (result == 1) {
      resultText.innerHTML = "Oh noz, you won. Why??? 😱😭😵🤬🤢👿";
      resultGif.src = "https://i.giphy.com/media/l1J9u3TZfpmeDLkD6/giphy.webp";
    } else if (result == 0){
        resultText.innerHTML = "It's a draw 🫤";
        resultGif.src = "https://i.giphy.com/media/wID3zXURLH1jrjCcZy/giphy.webp";
    } else {
      resultText.innerHTML = "Uh .... something went wrong? Sowwy."
      resultGif.src = "https://media4.giphy.com/media/RUCiI1kRfXfRUaFr6V/giphy.gif";
    }

    //Showing results while hiding action buttons.
    document.getElementById("results").classList.remove("hidden");
    document.getElementById("play-buttons").classList.add("hidden");
  }

  /** Game Helper Functions **/

  /*
   * Adds card to given player's cards.
   * Creates new card element and assigns to given player DOM
   * Returns total.
   */
  function addCard(plyr) {
    dealt = deal();
    plyr.cards.push(dealt);
    let playerElem = document.getElementById("game-board").children[1];
    if (plyr.name == dealer.name) {
      playerElem = document.getElementById("game-board").children[0];
    }

    const card = document.createElement("p")
    p.innerHTML = royals(dealt);
    p.classList.add("card");

    playerElem.children[1].appendChild(card);
    return sumTotal(plyr.cards);
  }
  
  /*
   * First checks for player name (handled by python)
   * If name > 4 chars, unhides game boards and sets up initial cards
   * Also sets player name in object then returns whether or not user needs to enter name.
   */
  function nameCheck() {
    let name = document.getElementById("player").children[0];
    if(name == "") { //Not blank
      alert("Enter a name, soldier.");
      return false; //Using continue because I don't want an else statement. Less indents.
    } else if (name.length < 4) { //Less than 4 chars
      alert("Enter a real name, solider. That means more than 4 characters.");
      return false;
    }
    player.name = name;
    return true;
  }
  /*
   * Generates Deck. It's 1d.
   * #Suits don't matter.
   * #Adds 4 of each 2-16 into an array
   * #Returns a shuffled array
   */
  function generateDeck() {
    let deck = []
    for (let i = 2; i < 15; i++) {
      for (let j=0; j<4; j++) {
        deck.push(i);
      }
    }
    return shuffle(deck);
  }

  /*
   * #Takes a deck array
   * #Returns and removes the last element of the array
   */
  function deal() {
    return deck.pop();
  }

  /*
   * Converts numbers to royals
   * Returns number if not a royal
   */
  function royals(cards) {
    cards.forEach((card) => {
      if (card == 11) {
        return 'J';
      } else if (card == 12) {
        return 'Q';
      } else if (card == 13) {
        return 'K';
      } else if (card == 14 || card == 1) { //Card should never equal 1, but you never know
        return 'A';
      }

      return card;
    });

    return newCards;
  }

  /*
   * Checks the total of the cards`
   * Resturns the sum, as per blackjack rules
   * Player object function
   */
  function sumTotal(cards) {
    sum = 0;
    cards.forEach((arg) => {
        //Handles 11 (ace) going above 21
        if (arg == 14 and sum+11 > 21) {
          sum += 1;
        } else if (arg == 14) { //Handles Ace
          sum += 11;
        } else if (arg >= 10) { //Handles other royals
          sum += 10;
        } else {
          sum += arg;
        }
    });

    return sum;
  }

  /*
   * Standard compareTo function customized for blackjack
   * a is positive
   * b is negative
   * if someway, somehow a & b are both > 21, it'll return null.
   * I don't know how that could possibly happen.
   */
  function compareTo(a, b) {
    if ((b > 21 && a <= 21) || a > b) {
      return 1;
    } if ((b <= 21 && a > 21) || a < b) {
      return -1;
    } if (a == b) {
      return 0;
    }
    return null;
  }

  /**
 * Shuffles array in place.
 * @param {Array} a items An array containing the items.
 * Taken from https://stackoverflow.com/questions/6274339/how-can-i-shuffle-an-array
 */
function shuffle(a) {
    var j, x, i;
    for (i = a.length - 1; i > 0; i--) {
        j = Math.floor(Math.random() * (i + 1));
        x = a[i];
        a[i] = a[j];
        a[j] = x;
    }
    return a;
}
});
