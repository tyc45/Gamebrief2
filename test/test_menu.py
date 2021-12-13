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

class TestMenu:
    def test_welcome_player(self,monkeypatch, capsys):
        """testing input player name, we will a string
        monkeypatch can replace the input for lamba for testing"""
        monkeypatch.setattr('builtins.input', lambda x : "Joe")
        Menu().welcome_player()
        captured = capsys.readouterr()
        assert captured.out == "Hello Joe, we are waiting you!\n"

    def test_game_start(self,monkeypatch,capsys):
        """testing the main game. He shoulds be return a different print depending of the player choice.
        1) launch the game 
        2) view score ( must be test in another fonction)
        3) quit the game"""
        monkeypatch.setattr('builtins.input', lambda x : 1)
        Game()
        captured = capsys.readouterr()
        assert captured.out == "In a distant land, you were just an adventurer in search of glory. You were about to abandon your quest to settle down as a baker in a small village ... When the chance to turn and you are in front of...\n"
        #test choose 3
        monkeypatch.setattr('builtins.input', lambda x : 3)
        Menu().exit_game()
        captured = capsys.readouterr()
        assert captured.out =="Good bye, see you later!\n" 

    def test_game_start_with_differents_input(self, monkeypatch, capsys):
        monkeypatch.setattr('builtins.input', lambda x : 6)
        Menu().start_game()
        captured = capsys.readouterr()
        assert captured.out =="Sorry Sir, I don't understand your choice\n" 

        monkeypatch.setattr('builtins.input', lambda x : "choix")
        Menu().start_game()
        captured = capsys.readouterr()
        assert captured.out =="Sorry Sir, I don't understand your choice\n"

def test_show_score(self, monkeypatch):
      """testing opening text.txt where is storage scores of player"""
    #     monkeypatch.setattr('builtins.input', lambda x : 2)
    #     assert Menu.game_menu() 
    #     with TempDirectory() as d:
    #         d.write('text.txt', b'Jean Sans Peur 200')
    #         d.read('text.txt')== b'Jean Sans Peur 200'
    #         d.cleanup()
