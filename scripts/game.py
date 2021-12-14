from dataclasses import dataclass, field
from .player import Player
from .bestiary import Goblin

@dataclass
class Game:
    """This is where the actual gameplay happens, mots methods here are here to make the game progress
    """    
    player_name: str
    _player: Player = field(init=False)
    _goblin: Goblin = field(init=False)
    # list_enemy

    def __post_init__(self):
        self.new_game()
    
    def new_game(self):
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
        print(f'You have {self.player.player_hp} HPs et your enemy has {self.goblin.health_points} HPs.')
        self.player_choice()
    
    
    def player_choice(self) -> None:
        """The main battle menu
        """        
        choice = input('What do you want? 1: Attack. 2: Use potion. 3: Infos')
        if str(choice) == '1':
            dmg = self.player.player_attack(self.goblin)
            print(f'You deal {dmg} damage to {self.goblin.name}!')
            if self.goblin.health_points <= 0:
                self.enemy_death()

        elif str(choice) == '2':
            heal = self.player.use_potion()
            print(f'You healed for {heal} HP')

        elif str(choice) == '3':
            self.display_infos()
            self.player_choice()
        else:
            print("I don't unterstand, can you repeat please?")
            self.player_choice()
        self.enemy_choice()


    def display_infos(self):
        """This is called when the player wants to know more about the game state
        """        
        print(f"You have: {self.player.player_hp} HP, your attack deals : 5-10 damage points")
        print(f"You enemy has : {self.goblin.health_points} HP, he can deal between: {self.goblin.min_attack} and {self.goblin.max_attack} damage points")

    
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
            self.new_game()       

    def enemy_death(self) -> None:
        """What happens when player kills all enemies
        """        
        print(f'Congratulations, you win! You beat {self.goblin.name}!')
        self.save_score()

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
    
    