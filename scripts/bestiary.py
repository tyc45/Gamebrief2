from dataclasses import dataclass, field
from enemy import Enemy

@dataclass
class Goblin(Enemy):
    _health_points: int = 50
    _min_attack: int = 5
    _max_attack: int = 15