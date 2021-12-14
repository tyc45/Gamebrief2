import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir)

from bestiary import Goblin, Harpy, GiantPython
from player import Player


@pytest.fixture
def goblin_test():
    return Goblin("Bobby", "Bobby just wants to make friends")

@pytest.fixture
def harpy_test():
    return Harpy("Aello", "she has a very beautiful voice but she is so ugly")

@pytest.fixture
def geant_python_test():
    return GiantPython("Indentation", "He is so useful but sometimes he makes you crazy")

@pytest.fixture
def player_test():
    return Player("David")

class TestEnemy:
    def test_enemy_health_points(self, goblin_test):
        assert goblin_test.health_points == 50
        with pytest.raises(ValueError):
            goblin_test.health_points = 0

    def test_enemy_min_attack(self, harpy_test):
        assert harpy_test.min_attack == 10
        with pytest.raises(ValueError):
            harpy_test.min_attack = 5
    
    def test_enemy_max_attack(self, geant_python_test):
        assert geant_python_test.max_attack == 27
        with pytest.raises(ValueError):
            geant_python_test.max_attack = 1
        
    def test_attack(self, enemy_test, player_test):
        assert harpy_test.attack(player_test) == player_test.player_hp

    def test_healing(self, goblin_test):
        assert goblin_test.healing(20) == 70
    def test_healing_two(self, enemy_test):
        assert goblin_test.healing(-5) == 45
    def test_healing_three(self, enemy_test):
        assert goblin_test.healing(10) == 60