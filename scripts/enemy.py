from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
import random

@dataclass
class Enemy(metaclass = ABCMeta):

    name: str
    description: str
    # max_health_points: int
    _health_points: int
    _min_attack: int
    _max_attack: int

    @property
    def health_points(self) -> int:
        return self._health_points
    
    @health_points.setter
    def health_points(self, hp):
        if hp < 0:
            raise ValueError("health_points should be positive")
        else: self._health_points = hp
    
    @property
    def min_attack(self) -> int:
        return self._min_attack
    
    @min_attack.setter
    def min_attack(self, min):
        if self._max_attack and self._max_attack < min or min < 0:
            raise ValueError("min_attack should be lower than max_attack")
        else: 
            self._min_attack = min
    
    @property
    def max_attack(self) -> int:
        return self._max_attack
    
    @max_attack.setter
    def max_attack(self, max):
        if type(max) != int:
            raise ValueError("max_attack should be an int")
        elif max < self.min_attack:
            raise ValueError("max_attack should be greater than min_attack!")
        else: 
            self._max_attack = max
            
            
    @abstractmethod
    def attack(self, player):
        """Enemy attacks a player

        Args:
            player (Player): The player this ennemy attacks
        """                
        dmg = random.randint(self.min_attack, self.max_attack)
        player.take_damage(dmg)
        return dmg
    
    def healing(self, heal):
        """This heals the enemy

        Args:
            int (int): The amount of life healed
        """        
        self.health_points += heal
        return self.health_points