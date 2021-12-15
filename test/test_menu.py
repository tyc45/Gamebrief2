import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir) 

from menu import Menu
from game import Game

def no_func(self):
    pass
class TestMenu:
    def test_welcome_player_one(self,monkeypatch, capsys):
        """testing input player name, we will a string
        monkeypatch can replace the input for lamba for testing"""
        monkeypatch.setattr('builtins.input', lambda x : "Joe")
        monkeypatch.setattr(Menu, 'start_game', no_func)
        Menu().welcome_player()
        captured = capsys.readouterr()
        assert captured.out == "\nWelcome Joe, we were waiting for you!\n\n"
    
    def test_welcome_player_two(self,monkeypatch, capsys):
        """testing input player name, we will a string
        monkeypatch can replace the input for lamba for testing"""
        monkeypatch.setattr('builtins.input', lambda x : "Joe")
        monkeypatch.setattr(Menu, 'start_game', no_func)
        menu = Menu()
        menu.player_name = "Joe"
        menu.welcome_player()
        captured = capsys.readouterr()
        assert captured.out == "\nWelcome back Joe, how are you today?\n\n"

    def test_exit_game(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda x : 3)
        Menu().exit_game()
        captured = capsys.readouterr()
        assert captured.out =="Good bye, see you later!\n"  

    def test_show_scores(self):
        """save.txt exists? """  
        assert os.path.exists(os.path.join(parentdir,"save.txt")) == True

    #TODO: Find a way to work with recursive functions, maybe needs to avoid the recursion altogether in main code
    # def test_start_game_1(self, monkeypatch, capsys):
    #     monkeypatch.setattr('builtins.input', lambda x : 4)
    #     Menu().start_game()
    #     captured = capsys.readouterr()
    #     assert captured.out == "Sorry pal, I don't understand... Try again..."