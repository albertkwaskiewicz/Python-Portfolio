import pytest
from main import *


@pytest.fixture()
def empty_board():
    return create_game_board()


def test_create_game_board(empty_board):
    assert empty_board == '  |  |  \n---------\n  |  |  \n---------\n  |  |  \n'


def test_create_sign_container():
    container = create_sign_container()
    assert container == ['', '', '', '', '', '', '', '', '']


def test_get_sign_location_from_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    location = get_sign_location_from_user()
    assert location == 3


def test_assign_sign(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    board = create_game_board()
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


def test_is_game_over():
    pass
