from dataclasses import dataclass, field
from game import Game

@dataclass
class Menu():
  player_name : str = field(init= False)

  def welcome_player(self):
    """ input for player_name"""
    self.player_name = input("Hello! What is your name, adventurer?")
    print (f'Welcome {self.player_name}, we were waiting you!')
    self.start_game()
  
  def exit_game(self):
    print(f"Good bye, see you later!")

  def show_score(self):
    """open the file text where scores are storage"""
    with open("save.text") as save:
      print(save.read())
   

  def start_game(self):
    """this fonction is the main menu of the game. Call others fonctions to lauch the game, read scores and quit the game"""
    player_choice = input("1. Oui aller au combat \n2. Voir les scores \n3. Quitter le jeu.\n")
    if player_choice == "1":
      Game(self.player_name)
      self.start_game()
    elif player_choice == "2":
      self.show_score()
      self.start_game()
    elif player_choice == "3":
      self.exit_game()
    else:
      print("Sorry, Sir I don't understand... Try again...")
      self.start_game()








    
    
    

    