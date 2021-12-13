from dataclasses import dataclass, field
from typing import ClassVar
from player import Player
from bestiary import Goblin
from menu import Menu

@dataclass
class Game:
    player_name: str
    player: Player = field(init=False)
    goblin: Goblin = field(init=False)
    # list_enemy

    def __post_init__(self):
        player = Player(self.player_name)
        goblin = Goblin('Bobby', 'a Goblin')
        print(f'In a distant land, you were just an adventurer in search of glory. You were about to abandon your quest to settle down as a baker in a small village ... When the chance to turn and you are in front of {goblin.name}, {goblin.description}')

    def score(self) -> int:
        score_game = self.player.player_hp + (self.player.player_inventory*50)
        return score_game

    def save_score(self) -> None:
        with open("save.txt", "a") as save:
            save.write('\n' + self.player.player_name + " " + str(self.score()))
    
    def player_death(self) -> None:
        print('Game over!')
        choice = input('Press 1 to play again')
        if choice == 1:
            Game(self.player.player_name)
        else:
            Menu(self.player.player_name)
        

    def enemy_death(self) -> None:
        print('Bravo vous avez gagné')
        self.save_score()
        Menu()
    
    def player_choice(self) -> None:
        """The main battle menu
        """        
        choice = input('Quel est votre choix? 1: Attaque. 2: Potion')
        if choice == 1:
            dmg = self.player.player_attack(self.goblin)
            print(f'Vous infligez {dmg} dégâts à {self.goblin.name}!')
        elif choice == 2:
            heal = self.player.use_potion()
            print(f'Vous vous êtes soigné de {heal} PV')
        else:
            print("Ce n'est pas un choix valide!")
            self.player_choice()
        enemy_choice()
    
    def enemy_choice(self):

    def display(self)
