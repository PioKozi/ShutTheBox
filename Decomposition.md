* Roll dice
  * randint()
  * Pictures
* Switches
  * buttons
  * toggled enabled/disabled to prevent illegal moves
* Make sure moves are legal
  * Switches toggled enabled/disabled to prevent illegal moves
* Check for bust
  * after roll, check if there are any legal moves
* check if game is won
  * check if there are nay switches in up state
* Make sure rollDice only occurs after at least one change
  * have an updateDictionary, which must have updates from the original dictionary of switches
  * use if dictionary.update(updateDictionary) == dictionary:
