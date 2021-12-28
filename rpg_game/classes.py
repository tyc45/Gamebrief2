import random
from rpg_game.player import Player
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class Adventurer(Player):
    player_hp: ClassVar[int] = 50
    player_inventory: ClassVar[int] = 3

    def player_attack(self, enemy):
        """ 
        This function remove a random number of HP between 5 and 10 to the enemy
        """
        dmg = random.randint(5, 10)
        enemy.take_damage(dmg)
        return dmg
    
    def take_damage(self, dmg):
        """Function that deals with damage received

        Args:
            dmg (int): The amount of damage the enemy intends to deal
        """        
        self.player_hp -= dmg
    
    def use_potion(self):
        """
        This function adds HP to the player if he chooses to
        """
        if self.player_inventory > 0:
            heal = random.randint(15, 50)
            self.player_hp += heal
            self.player_inventory -= 1
            if self.player_hp>50:
                self.player_hp = 50
            return heal

class Wizard(Player):
    player_hp: ClassVar[int] = 40
    player_mana: ClassVar[int] = 30

    def player_attack(self, enemy):
        """ 
        This function remove a random number of HP between 5 and 10 to the enemy
        """
        dmg = random.randint(3, 8)
        enemy.take_damage(dmg)
        return dmg
    
    def take_damage(self, dmg):
        """Function that deals with damage received

        Args:
            dmg (int): The amount of damage the enemy intends to deal
        """        
        self.player_hp -= dmg+2
    
    def fireball(self):
        """
        This function adds HP points to the player if he chooses to
        """
        if self.player_mana >= 5:
            dmg = random.randint(8, 16)
            self.player_mana -= 5
            return dmg
    
    def heal(self):
        if self.player_mana >= 10:
            heal = random.randint(15, 35)
            self.player_hp += heal
            self.player_mana -= 10
            return heal


@dataclass
class Ranger(Player):
    player_hp: ClassVar[int] = 45
    player_darts: ClassVar[int] = 3

    
    def crit(self, die):
        return random.randint(1,die) == die

    def player_attack(self, enemy):
        """ 
        This function remove a random number of HP between 5 and 10 to the enemy
        """
        dmg = random.randint(5, 12)
        if self.crit(6): dmg *= 2
        enemy.take_damage(dmg)
        return dmg
    
    def take_damage(self, dmg):
        """Function that deals with damage received

        Args:
            dmg (int): The amount of damage the enemy intends to deal
        """   
        if not self.crit(6):
            self.player_hp -= dmg+2