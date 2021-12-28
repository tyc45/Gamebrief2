from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import ClassVar
import random

@dataclass
class Player(metaclass = ABCMeta):
    player_name: str
    player_hp: ClassVar[int]

    @property
    def player_name(self) -> str:
        return self._player_name
    
    @player_name.setter
    def player_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name should be a string of characters")
        else:
            self._player_name = value
    
    @abstractmethod
    def player_attack(self, enemy):
        """ 
        This function remove a random number of HP between 5 and 10 to the enemy
        """
        pass
    
    @abstractmethod
    def take_damage(self, dmg):
        """Function that deals with damage received

        Args:
            dmg (int): The amount of damage the enemy intends to deal
        """        
        pass
    

    # def check_inventory(self):
    #         """
    #         Checking if the player have enough potions
    #         """
    #         if self.player_inventory > 0:
    #             self.player_hp = self.use_potion()
    #             self.player_inventory -= 1
    #         else:
    #             print("Sorry, you don't have any potion left")

    # def check_infos(self, enemy):
    #     """
    #     This function print informations about the player's pv
    #     (and the number of potions he has ) and the monster's pv.
    #     """
    #     print(f"{self.player_name}, il vous reste {self.player_hp} points de vie et {self.player_inventory} potion(s), le Troll a {enemy.enemy_pv} points de vie.")