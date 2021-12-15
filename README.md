# Brief_Game
## Context

This game is an achieved project by three students of Simplon Lille ( France.) We are students of the 2nd session of IA technicians. We started learning  Python. This project is about python basics ( particulary functions and tests.)

## The game

You are a adventurer and you are fighting against a little and ugly goblin. You and the goblin have both 50 life points.

On your turn you can choose between attacking the goblin or you can drink a heal potion who restore between 15 and 50 life points to your character. The attack can afflict 5 to 10 damage points to the goblin. Warning! you just have only three heal potions, use them wisely in your journey.
After, it's the goblin's turn. He attacks you and you loose between 5 and 15 life points.

The party is over when you or the goblin run out of life points.

## Configuration 

This is a game for your terminal. It's based on the version python 3.8 (Python 3.8.8 64-bit ('base':conda)).

Testing by pytest and we use the random library.

## Installation

Clone this repository and open it.
Run the file main.py 
Enjoy our little game.

## File details

This folder contains :
-main.py to launch the game (it launches the class Menu)
-bestiary.py adds or maintains monsters (right now we only use the goblin)
-enemy.py for the Enemy class and its methods (= enemy turn)
-player.py for the Player class and its methods (= player turn)
-menu.py for the game's main menu
-game.py for the Game class. This files contains methods relating to the game mechanism: turn sequencing and end of the game (by the death of the player or enemy). It also contains the calculation and storage of the score
The tests are organized in the tests folder. Each file corresponds to the class it tests except bestiary which is tested within the same file as enemy.