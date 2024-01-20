# Battleships
Link to deployed app: https://battleships-bgc-a8f0f32ea97f.herokuapp.com/

mockups here

### User Demographic
The Battleships game is intended for any user. 

### Purpose
Battleships is a classic game. This version is written for a human user vs a computer opponent. 

### Instructions


### Features


### Future development


### Data model/Technologies/structures used

## Testing

The following tests were carried out to ensure succesful operation and deployment of the app.

All tests achieved the expected result (pass).

| Function                    | Test                                           | Result |
|-----------------------------|------------------------------------------------|--------|
| Enter username              | Enter less than 3 characters                   | Given error message and a chance to try again|
|                             | Enter more than 8 characters                   | Given error message and a chance to try again|
|                             | No value entered                               | Given error message and a chance to try again|
|                             | Enter incorrect character (number of symbol)   | Given "invalid charcters" error message and a chance to try again|
|                             | Enter username between 3 - 8 letters           | Greeting displayed and game options displayed|
| Game Options                | Incorrect number entered (3 or above)          | Error message "Incorrect choice" displayed and re-prompt for user input|
|                             | Negative number entered (-1 or lower)          | Error message "Incorrect choice" displayed and re-prompt for user input|
|                             | Single or multiple Letter entered              | Error message "Incorrect choice" displayed and re-prompt for user input|
|                             | Symbol entered                                 | Error message "Incorrect choice" displayed and re-prompt for user input|
|                             | No value entered                               | Error message "Incorrect choice" displayed and re-prompt for user input|
|                             | '1' entered                                    | "Running the game" message displays. Game starts correctly|
|                             | '2' entered                                    | Instructions of the game are displayed then user re-prompt for game options|
| Re-prompt game options      | Tested as Game Options above                   | All tests passed|
| Choose player coordinates   | aa bb cc (just chars)                          | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | 11 66 99 (just numbers)                        | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | 12 15 48 965 52                                | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | cf 4g h8 d2 f89 (mix of correct/incorrect vals)| "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | a1 a2 a3 a4 a4 (repeat entries)                | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | a1,b4..Correct vals separated by comma         | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | Correct vals separated by double space         | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | Symbols entered                                | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | No value entered                               | "Incorrect coordinates entered.." error message displayed. Re-prompt user for correct values|
|                             | Correct coords with uppercase letters          | "All coordinates match required format" message displayed. Game continues|
|                             | Correct coords with lowercase letters          | "All coordinates match required format" message displayed. Game continues|
| Press ENTER to start the game| "Enter" pressed                                | Game continues|
|                             | Any other key entered                          | Nothing happens until "Enter" is pressed. Then game continues|
| Player shot (user input)    | Double letter entered (aa or hh or ty)         | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | Double number entered (22, 56, 89)             | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | 3 or more letters entered (abc)                | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | 3 or more numbers entered (637)                | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | Symbols entered (a£, g", (6, ,,)               | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | Out of range coord enetered (h9, l2)           | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | No value entered                               | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | More than one correct coordinate entered       | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | Repeated value entered                         | "You already tried that one" displayed. Re-prompt user for correct values|
|                             | Enter pressed before the prompt                | "Invalid coordinates!!!" message displayed. Re-prompt user for correct values|
|                             | Correct value entered (a1 to h8 tried)         | Game continues. Hit/Miss recorded and score updated as expected| 
| Press ENTER to continue..   | "Enter" pressed                                | Game continues|
|                             | Any other key entered                          | Nothing happens until "Enter" is pressed. Then game continues|
| Coordinate is a Miss        | Coordinate doesn't match opponents ship        | Player/Cpu (current player) guess board updated with 'O', 'Miss' displayed. Score updated. Game continues|
| Coordinate is a Hit         | Coordinate matches opponents ship              | Player or Cpu (current player) guess board updated with 'X'. 'Hit' displayed. Score updated. Game continues|
| All other player shots      | Tested as player shot above                    | Results as Player Shot above. Game continues|
| Endgame choice              | Invalid number entered (8, 967)                | "Invalid choice" displayed. Re-prompt user for correct value|
|                             | Invalid character entered (G, $, ;)            | "Invalid choice" displayed. Re-prompt user for correct value|
|                             | No value entered                               | "Invalid choice" displayed. Re-prompt user for correct value|
|                             | Negative value entered (-1, -2)                | "Invalid choice" displayed. Re-prompt user for correct value|
|                             | '1' entered                                    | Game restarts after message and countdown displayed|
|                             | '2' entered                                    | Game exits after message is displayed|


## Bugs


### Solved Bugs
| Bug                                                       | Solution                                          |
|-----------------------------------------------------------|---------------------------------------------------|
| The score wasn't updating in game                         | Score was only being updated at start of game. Moved inside game while True loop.|
| Guess boards being updated incorrectly                    | Adjust [row] to [row - 1] to compensate.|
| end_game() creating an infinte loop                       | Move user input inside the while loop.|
| os.system('clear') not working on all os's                | Import sys library. Add a clear() function to ensure app works accross windows, macos and linux.|
  

### Existing bugs
I have not been able to identify any existing bugs.

### pep8 validation


### Manual Testing Outcome report


## Deployment Steps


## Credits



