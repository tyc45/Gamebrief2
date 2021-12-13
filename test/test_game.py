import pytest 
import os
import sys
import inspect
import re

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir)

from bestiary import Goblin
from player import Player
from game import Game

@pytest.fixture
def game_test():
    return Game('test_player')


class TestGame:
    def test_init(self, game_test):
        assert game_test.player_name == 'test_player'
        assert isinstance(game_test.player, Player)
        assert isinstance(game_test.goblin, Goblin)

    def test_turn_start(self, game_test, capsys):
        game_test.turn_start()
        captured = capsys.readouterr()
        assert captured.out == f"Vous avez {game_test.player.player_hp} PVs et votre adversaire a {game_test.goblin.health_points}."
    
    def test_player_choice(self, game_test, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: "1")
        assert re.search(f"Vous infligez \d+ dégâts à {game_test.goblin.name}!'", game_test.player_choice()) != None