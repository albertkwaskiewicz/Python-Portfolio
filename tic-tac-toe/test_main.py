import pytest
from main import *


@pytest.fixture()
def empty_board():
    return create_game_board()


def test_create_game_board(empty_board):
    assert empty_board == '  |  |  \n---------\n  |  |  \n---------\n  |  |  \n'


def test_create_sign_container():
    container = create_sign_container()
    print(container)
    assert container == [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def test_get_sign_location_from_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    location = get_sign_location_from_user()
    assert location == 3

@pytest.mark.skip('Have to restructure sign container')
def test_assign_sign(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    container = create_sign_container()
    board = assign_sign('X', container)
    assert board == '  |  | X \n---------\n  |  |  \n---------\n  |  |  \n'
    assert container == ['', '', 'X', '', '', '', '', '', '']


def test_update_board():
    container = ['', '', 'X', '', '', '', '', '', '']
    board = update_board(container)
    print(board)
    print('  |  | X \n---------\n  |  |  \n---------\n  |  |  \n')
    assert board == '  |  | X \n---------\n  |  |  \n---------\n  |  |  \n'


@pytest.mark.parametrize('game_over', [
    ['X', 'X', 'X', '', '', '', '', '', ''],
    ['', '', '', 'X', 'X', 'X', '', '', ''],
    ['', '', '', '', '', '', 'X', 'X', 'X'],
    ['X', '', '', 'X', '', '', 'X', '', ''],
    ['', 'X', '', '', 'X', '', '', 'X', ''],
    ['', '', 'X', '', '', 'X', '', '', 'X'],
    ['', '', 'X', '', 'X', '', 'X', '', ''],
    ['X', '', '', '', 'X', '', '', '', 'X'],
    ['X', 'O', 'X', 'O', 'O', 'X', 'X', 'X', 'O']
])
@pytest.mark.skip()
def test_is_game_over(game_over):
    # assert is_game_over(game_over)
    pass
