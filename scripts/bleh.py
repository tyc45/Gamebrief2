from bestiary import Goblin
from dataclasses import dataclass, field


gob = Goblin("Bobby", "Bobby just wants to make friends")
gob.health_points = 0
print(gob.health_points)
