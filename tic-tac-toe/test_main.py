import pytest
import main

def test_create_game_board():
    board = main.create_game_board()
    assert board == '''
       |   |   
    -----------
       |   |   
    -----------
       |   |   
    '''