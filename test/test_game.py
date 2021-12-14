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

def no_func(self):
    pass


class TestGame:

    def test_init(self, monkeypatch):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        game_test = Game('test_player')
        assert game_test.player_name == 'test_player'
        assert isinstance(game_test.player, Player)
        assert isinstance(game_test.goblin, Goblin)

    def test_turn_start(self, capsys, monkeypatch):        
        monkeypatch.setattr(Game, 'player_choice', no_func)
        game_test = Game('test_player')
        captured = capsys.readouterr()
        assert re.search(f"Vous avez {game_test.player.player_hp} PVs et votre adversaire a {game_test.goblin.health_points}.", captured.out) != 1
    
    def test_player_choice_one(self, capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: 1)
        monkeypatch.setattr(Game, 'enemy_choice', no_func)
        captured = capsys.readouterr()
        Game('test_player')
        assert re.search(r"Vous infligez \d+ dégâts à ", captured.out) != -1
    
    def test_player_choice_two(self, capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: 2)
        monkeypatch.setattr(Game, 'enemy_choice', no_func)
        captured = capsys.readouterr()
        Game('test_player')
        assert re.search(r'Vous vous êtes soigné de \d+ PV', captured.out) != -1

    # def test_player_choice_three(self, capsys, monkeypatch):
    #     monkeypatch.setattr('builtins.input', lambda x: 1)
    #     monkeypatch.setattr(Game, 'enemy_choice', no_func)
    #     captured = capsys.readouterr()
    #     Game('test_player')
    #     assert re.search(r"Vous infligez \d+ dégâts à ", captured.out) != -1


    def test_display_infos(self, monkeypatch, capsys):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        captured = capsys.readouterr()
        Game('test_player')
        assert re.search(r"Vos PVs actuels: 50, votre attaque actuelle: 5-10", captured.out) != -1
        assert re.search(r"Les PVs de l'enemi: 50, l'attaque de l'enemi: 5-15", captured.out) != -1

    def test_enemy_choice(self, monkeypatch):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        game_test = Game('test_player')
        game_test.enemy_choice()
        assert 35 <= game_test.player.player_hp < 50

    # def test_player_death(self):
    #     with pytest.raises(TypeError):
    #         game_test.player_death.choice = str
    #         game_test.player_death.choice = float
    #         game_test.player_death.choice = bool

    # def test_enemy_death(self):
    #     pass

    def test_score(self, monkeypatch):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        game_test = Game('test_player')
        assert game_test.score() == 200

    def test_save_score(self, monkeypatch):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        game_test = Game('test_player')
        game_test.save_score()
        assert os.path.exists(os.path.join(parentdir,"save.text")) == True