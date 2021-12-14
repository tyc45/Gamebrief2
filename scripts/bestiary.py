from dataclasses import dataclass, field
from enemy import Enemy

@dataclass
class Goblin(Enemy):
    _health_points: int = 50
    _min_attack: int = 5
    _max_attack: int = 15

    def attack(self, player):
        """The most basic attack

        Args:
            player (Player): The attacked player
        """        
        dmg = super().attack(player)
        print(f"{self.name} the goblin hurls at you for {dmg} damage")
        return player.player_hp

@dataclass
class Harpy(Enemy):
    _health_points: int = 125
    _min_attack: int = 10
    _max_attack: int = 25

    def attack(self, player):
        """The most basic attack
        Args:
        player (Player): The attacked player
        """        
        dmg = super().attack(player)
        print(f"{self.name} the queen harpy scratches you and you loose {dmg} PV's.")
        return player.player_hp

@dataclass
class GiantPython(Enemy):
    _health_points: int = 150
    _min_attack: int = 15
    _max_attack: int = 27

    def attack(self, player):
        """The most basic attack

        Args:
        player (Player): The attacked player
        """        
        dmg = super().attack(player)
        print(f"{self.name} creates a big bug in your code, you cry and loose {dmg} PV's.")
        return player.player_hp    
    
