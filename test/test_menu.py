import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir) 

from menu import Menu 

class TestMenu():
    def test_welcome_player(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda x : "John Do")
        assert Menu.welcome_player() == 'ok John Do we were waiting for you!'

    @pytest.fixture
    def menu_test():
        return Menu()
    
    def test_menu():
        

    
    
    # def test_menu():
    #     pass
