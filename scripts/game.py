from dataclasses import dataclass, field
from typing import ClassVar
from player import Player
from bestiary import Goblin
from menu import Menu

@dataclass
class Game:
    """This is where the actual gameplay happens, mots methods here are here to make the game progress
    """    
    player_name: str
    _player: Player = field(init=False)
    _goblin: Goblin = field(init=False)
    # list_enemy

    def __post_init__(self):
        self.player = Player(self.player_name)
        self.goblin = Goblin('Bobby', 'a Goblin')
        print(f'In a distant land, you were just an adventurer in search of glory. You were about to abandon your quest to settle down as a baker in a small village ... When the chance to turn and you are in front of {self.goblin.name}, {self.goblin.description}')
        self.turn_start()
    
    @property
    def player_name(self) -> str:
        return self._player_name

    @player_name.setter
    def player_name(self, name:str):
        if isinstance(name, str):
            self._player_name = name   
        else:
            self._player_name = 'Player 1'

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        
    @property
    def goblin(self) -> Goblin:
        return self._goblin

    @goblin.setter
    def goblin(self, goblin):
        if isinstance(goblin, Goblin):
            self._goblin = goblin


    def turn_start(self) -> None:
        """Method called at each turn start
        """        
        print(f'Vous avez {self.player.player_hp} PVs et votre adversaire a {self.goblin.health_points}.')
        self.player_choice()
    
    
    def player_choice(self) -> None:
        """The main battle menu
        """        
        choice = input('Quel est votre choix? 1: Attaque. 2: Potion. 3: Infos')
        if choice == 1:
            dmg = self.player.player_attack(self.goblin)
            print(f'Vous infligez {dmg} dégâts à {self.goblin.name}!')
            if self.goblin.health_points <= 0:
                self.enemy_death()

        elif choice == 2:
            heal = self.player.use_potion()
            print(f'Vous vous êtes soigné de {heal} PV')

        elif choice == 3:
            self.display_infos()
            self.player_choice()

        else:
            print("Ce n'est pas un choix valide!")
            self.player_choice()
        self.enemy_choice()


    def display_infos(self):
        """This is called when the player wants to know more about the game state
        """        
        print(f"Vos PVs actuels: {self.player.player_hp}, votre attaque actuelle: 5-10")
        print(f"Les PVs de l'enemi: {self.goblin.health_points}, l'attaque de l'enemi: {self.goblin.min_attack}-{self.goblin.max_attack}")

    
    def enemy_choice(self):
        """The enemy's reactions to player's actions
        """        
        self.goblin.attack(self.player)
        if self.player.player_hp <= 0:
            self.player_death()
        else:
            self.turn_start()

 
    def player_death(self) -> None:
        """What happens when player's HP drop to 0
        """        
        print('Game over!')
        choice = input('Press 1 to play again')
        if choice == 1:
            Game(self.player.player_name)
        else:
            Menu(self.player.player_name)        

    def enemy_death(self) -> None:
        """What happens when player kills all enemies
        """        
        print('Bravo vous avez gagné!')
        self.save_score()
        Menu()
    

    def score(self) -> int:
        """This calculates the score after a win

        Returns:
            int: The actual player's score
        """        
        score_game = self.player.player_hp + (self.player.player_inventory*50)
        return score_game

    def save_score(self) -> None:
        """This calls the score method then saves it to a txt
        """        
        with open("save.txt", "a") as save:
            save.write('\n' + self.player.player_name + " " + str(self.score()))
    
    