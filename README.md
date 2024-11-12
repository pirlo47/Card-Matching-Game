# Card-Matching-Game
Matches all pairs of cards by turning over two pairs of card at a time 
This is my first project on github 

This project involves a grid of face-down cards, where each card has a match hidden somewhere on the board. The player turns over two cards at a time, aiming to find matching pairs. 
THE PURPOSE IS TO UNDERSTAND TEST DRIVEN DEVELOPMENT 
disclaimer: NOT IMPLEMENETED FOR USER INPUT 

Here's an outline of the game:

1. Objective: Match all pairs of cards by turning over two cards at a time 
Gameplay:
- A grid of cards placed face down
- Select two cards in each turn to reveal 
- If two cards match, they stay face-up; otherwise, they flip back down 
- The game ends when all pairs are matched 

In this project, i will make use of test driven development with unittest 
Steps for TDD with unittest 
1. Define a board
- Write tests for generating a board with an even number of cards(e.g a 4x4 grid with 8 unique pairs)
-Ensure that each pair of cards appears atleast twice 

2. Card Selection 
- Write tests for a func that handles selecting two cards, ensuring they're within bounds and haven't already been matched 
- Test what happens when an invalid selection is made

3. Card Matching Logic 
- Write test for comparing the value of two selected cards 
- If they match, they should remain face-up, else, they should be turned face down 

4. Game Status 
- Write tests to determine when the game is completed 



