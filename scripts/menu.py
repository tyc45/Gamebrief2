from dataclasses import dataclass, field
from typing import ClassVar

import json

@dataclass
class Menu():
  player_name =  str

  def welcome_player(self):
    """ input for player_name"""
    self.player_name = input("Hello! What is your name, adventurer?")
    print (f'ok {self.player_name} we were waiting for you!')
  
  def exit_game(self):
    print(f"Good bye{self.player_name}, see you later!")

  def show_score(self):
    with open("save.json") as save:
      print(save.read())

  def menu(self):
    """this fonction is the main menu of the game. Call others fonctions for lauch game, read scores and quit the game"""
    player_choice = input("1. Oui aller au combat \n2. Voir les scores \n3. Quitter le jeu.\n")
    if player_choice == "1":
      return True
    elif player_choice == "2":
      show_score()
    elif player_choice == "3":
      exit_game()
    else:
      raise ValueError("Sorry, Sir I don't understand... Try again...")





    
    
    

    