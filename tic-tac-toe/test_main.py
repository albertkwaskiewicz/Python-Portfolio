import pytest
from main import *


def test_create_game_board():
    board = create_game_board()
    assert board == '''
       |   |   
    -----------
       |   |   
    -----------
       |   |   
    '''


def test_create_piece_container():
    container = create_piece_container()
    assert container == ['', '', '', '', '', '', '', '', '']


def test_get_piece_location_from_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    location = get_piece_location_from_user()
    assert location == 3