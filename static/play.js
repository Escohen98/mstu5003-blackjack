//Script used to handle the blackjack game in play.html
(function() {
  window.addEventListener("load", initialize);

  //Starts loading page with just a name field.
  function initialize() {
    let person = prompt("Enter your name, soldier")
    while(true) {
      if (person == null || person.length < 4) {
        alert()
      }
    }
    document.querySelector("#name").addEventListener("click", startGame);
  }

  function startGame() {
    let name = document.getElementById(name);
    if (name.value.length > 4) {
      let message =
    }
  }
});
