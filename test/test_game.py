import pytest 
import os
import sys
import inspect
import re

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir)

from rpg_game.bestiary import Goblin
from rpg_game.player import Player
from rpg_game.game import Game

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
        Game('test_player')
        captured = capsys.readouterr()
        assert re.search(r"You have \d+ HPs and your enemy has \d+.", captured.out) is not None
    
    def test_player_choice_one(self, capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: 1)
        monkeypatch.setattr(Game, 'enemy_choice', no_func)
        Game('test_player')
        captured = capsys.readouterr()
        assert re.search(r"test_player deals \d+ damage to \w+!", captured.out) is not None
    
    def test_player_choice_two(self, capsys, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x: 2)
        monkeypatch.setattr(Game, 'enemy_choice', no_func)
        Game('test_player')
        captured = capsys.readouterr()
        assert re.search(r'You healed for \d+ HP', captured.out) is not None


    def test_display_infos(self, monkeypatch, capsys):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        game_test = Game('test_player')
        game_test.display_infos()
        captured = capsys.readouterr()
        assert re.search(r"You have: \d+ HP, your attack deals : 5-10 damage points", captured.out) != None
        assert re.search(r"You enemy has : \d+ HP, he can deal between: \d+ and \d+ damage points", captured.out) != None

    def test_enemy_choice(self, monkeypatch):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        game_test = Game('test_player')
        game_test.enemy_choice()
        assert 35 <= game_test.player.player_hp < 50

    def test_player_death(self, monkeypatch, capsys):
        monkeypatch.setattr(Game, 'turn_start', no_func)
        Game().player_death
        capture = capsys.readouterr()
        assert re.search(r'In a distant land, you were just an adventurer in search of glory. You were about to abandon your quest to settle down as a baker in a small village ... When the chance to turn and you are in front of \w+,', capture.out) != None

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
        assert os.path.exists(os.path.join(parentdir,"save.txt")) == True