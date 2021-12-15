from dataclasses import dataclass, field
from game import Game

@dataclass
class Menu():
  player_name : str = field(init= False)

  def welcome_player(self):
    """ input for player_name"""
    if not hasattr(self, 'player_name'):
      self.player_name = input("Hello! What is your name, adventurer?\n\n")
      print (f'\nWelcome {self.player_name}, we were waiting for you!\n')
    else:
      print(f'\nWelcome back {self.player_name}, how are you today?\n')
    self.start_game()
  
  def exit_game(self):
    print(f"Good bye, see you later!")

  def show_score(self):
    """open the file text where scores are storage"""
    with open("save.txt") as save:
      print(save.read())
   

  def start_game(self):
    """this fonction is the main menu of the game. Call others fonctions to lauch the game, read scores and quit the game"""
    print("What do you want to do?\n")
    player_choice = input("1. Start a fight \n2. Check leaderboard \n3. Quit game\n")
    if player_choice == "1":
      Game(self.player_name)
      self.start_game()
    elif player_choice == "2":
      self.show_score()
      self.start_game()
    elif player_choice == "3":
      self.exit_game()
    else:
      print("Sorry pal, I don't understand... Try again...")
      self.start_game()