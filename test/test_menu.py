import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
brotherdir = os.path.join(parentdir, "scripts")
sys.path.insert(0, brotherdir) 

from menu import Menu 

class TestMenu:
    def test_welcome_player(self,monkeypatch):
        """testing input player name, we will a string"""
        monkeypatch.setattr('builtins.input', lambda x : "John Do")
        assert Menu.welcome_player() == 'ok John Do we were waiting for you!'
        with pytest.raises(TypeError):
            monkeypatch.setattr('builtins.input', lambda x : 12345)

    @pytest.fixture
    def menu_test():
        """create empty menu test """
        menu_test= Menu()
        return menu_test
    
    def test_menu(self):
        monkeypatch.setattr('builtins.input', lambda x : 1)

    monkeypatch.setattr('builtins.input', lambda x : 1)
