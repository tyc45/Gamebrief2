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
def giant_python_test():
    return GiantPython("Indentation", "He is so useful but sometimes he makes you crazy")

@pytest.fixture
def player_test():
    return Player("David")

class TestEnemy:
    def test_enemy_health_points(self, goblin_test):
        assert goblin_test.health_points == 50
        with pytest.raises(ValueError):
            goblin_test.health_points = -1

    def test_enemy_min_attack(self, harpy_test):
        assert harpy_test.min_attack == 10
        with pytest.raises(ValueError):
            harpy_test.min_attack = '1'
        with pytest.raises(ValueError):
            harpy_test.min_attack = 50
    
    def test_enemy_max_attack(self, giant_python_test):
        assert giant_python_test.max_attack == 27
        with pytest.raises(ValueError):
            giant_python_test.max_attack = 1
        with pytest.raises(ValueError):
            giant_python_test.max_attack = '20'
        
    def test__harpy_attack(self, harpy_test, player_test):
        assert harpy_test.min_attack <= harpy_test.attack(player_test) <= harpy_test.max_attack

    def test__goblin_attack(self, goblin_test, player_test):
        assert goblin_test.min_attack <= goblin_test.attack(player_test) <= goblin_test.max_attack

    def test__giant_python_attack(self, giant_python_test, player_test):
        assert giant_python_test.min_attack <= giant_python_test.attack(player_test) <= giant_python_test.max_attack