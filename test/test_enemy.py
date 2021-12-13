import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir)

from bestiary import Goblin
from player import Player


@pytest.fixture
def enemy_test():
    return Goblin("Bobby", "Bobby just wants to make friends")

@pytest.fixture
def player_test():
    return Player("David")

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
        
    def test_attack(self, enemy_test, player_test):
        assert enemy_test.attack(player_test) == player_test.player_hp

    def test_healing(self, enemy_test):
        assert enemy_test.healing(20) == 70
    def test_healing_two(self, enemy_test):
        assert enemy_test.healing(-5) == 45
    def test_healing_three(self, enemy_test):
        assert enemy_test.healing(10) == 60