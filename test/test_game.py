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
def game_test(monkeypatch):
    monkeypatch.delattr('scripts.game.Game.turn_start', raising=True)
    return Game('test_player')


class TestGame:
    def test_init(self, game_test):
        assert game_test.player_name == 'test_player'
        assert isinstance(game_test.player, Player)
        assert isinstance(game_test.goblin, Goblin)

    def test_turn_start(self, capsys, monkeypatch):
        # TODO: Figure out how to prevent the test from going too deep in functions
        monkeypatch.delattr(Game, 'player_choice', raising=True)
        game_test = Game('Jojo')
        game_test.turn_start()
        captured = capsys.readouterr()
        assert captured.out == f"Vous avez {game_test.player.player_hp} PVs et votre adversaire a {game_test.goblin.health_points}."
    
    def test_player_choice(self, game_test, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: "1")
        assert re.search(f"Vous infligez \d+ dégâts à {game_test.goblin.name}!", game_test.player_choice()) != None

    def test_display_infos(self, game_test):
        assert game_test.display_infos == f"Vos PVs actuels: 50, votre attaque actuelle: 5-10" + f"Les PVs de l'enemi: 50, l'attaque de l'enemi: 5-15"

    def test_enemy_choice(self):
        pass

    def test_player_death(self):
        with pytest.raises(TypeError):
            game_test.player_death.choice = str
            game_test.player_death.choice = float
            game_test.player_death.choice = bool

    def test_enemy_death(self):
        pass

    def test_score(self):
        assert game_test.score == 200

    def test_save_score(self):
        pass