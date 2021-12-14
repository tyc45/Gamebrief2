import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir) 

from menu import Menu

def no_func(self):
    pass
class TestMenu:
    def test_welcome_player(self,monkeypatch, capsys):
        """testing input player name, we will a string
        monkeypatch can replace the input for lamba for testing"""
        monkeypatch.setattr('builtins.input', lambda x : "Joe")
        monkeypatch.setattr(Menu, 'start_game', no_func)
        Menu().welcome_player()
        captured = capsys.readouterr()
        assert captured.out == "Welcome Joe, we were waiting you!\n"

    def test_exit_game(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda x : 3)
        Menu().exit_game()
        captured = capsys.readouterr()
        assert captured.out =="Good bye, see you later!\n"  

    def test_show_scores(self):
        """save.txt exist? """  
        assert os.path.exists(os.path.join(parentdir,"save.txt")) == True


