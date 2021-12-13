import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir)

from bestiary import Goblin


@pytest.fixture
def enemy_test():
    return Goblin("Bobby", "Bobby just wants to make friends")

class TestEnemy:
    def test_enemy_health_points(self, enemy_test):
        assert enemy_test.health_points == 50
        with pytest.raises(ValueError):
            enemy_test.health_points = 0

    def test_enemy_min_attack(self, enemy_test):
        assert enemy_test.min_attack == 5
        with pytest.raises(ValueError):
            enemy_test.min_attack = 20
    
    def test_enemy_max_attack(self, enemy_test):
        assert enemy_test.max_attack == 15
        with pytest.raises(ValueError):
            enemy_test.max_attack = 4