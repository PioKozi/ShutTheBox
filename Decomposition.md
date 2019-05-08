* Roll diceV
  * randint() V
  * Pictures V
* SwitchesV
  * buttonsV
  * toggled enabled/disabled to prevent illegal movesV
* Make sure moves are legalV
  * Switches toggled enabled/disabled to prevent illegal movesV
* Check for bust
  * after roll, check if there are any legal moves
  **Change of plans, if you are bust you simply cannot make a move**
* check if game is won
  * check if there are nay switches in up state
  **Change of plans, if you win you simply cannot make a move, and all switches are down-representing colour**
* Make sure rollDice only occurs after at least one changeV
  * have an updateDictionary, which must have updates from the original dictionary of switches V
  * use if dictionary.update(updateDictionary) == dictionary: V
