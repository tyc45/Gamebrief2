import pytest 
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir)
from player import Player

@pytest.fixture
def player_test():
    return Player("David")


class TestPlayer: 
    def test_init(self, player_test):
        assert player_test.player_name == "David"
        # assert player_test.player_hp() == 50
        with pytest.raises(ValueError):
            Player(50)
            Player(5.5)
        
    def test_player_attack(self, player_test):
        assert 30<=player_test.player_attack(45)<=40
        assert 25<=player_test.player_attack(40)<=35
        with pytest.raises(TypeError):
            player_test.player_attack("a",0,5.5)

    def test_use_potion(self, player_test):
        assert 40<=player_test.use_potion()<=50
        assert 27<=player_test.use_potion()<=50 
        assert 17<=player_test.use_potion()<=50

    def test_check_inventory(self):
        pass

    def test_check_infos(self):
        pass