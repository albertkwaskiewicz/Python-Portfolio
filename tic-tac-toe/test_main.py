import pytest
from main import *


@pytest.fixture()
def empty_board():
    return '   |   |   \n-----------\n   |   |   \n-----------\n   |   |   \n'

@pytest.fixture()
def x_in_3_board():
    return '   |   | X \n-----------\n   |   |   \n-----------\n   |   |   \n'
@pytest.fixture()
def empty_container():
    return [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


@pytest.fixture()
def one_sign_container():
    return [[' ', ' ', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]


@pytest.fixture()
def full_container():
    return [['X', 'O', 'X'], ['O', 'O', 'X'], ['X', 'X', 'O']]


def test_create_game_board(empty_board):
    assert create_game_board() == empty_board


def test_create_sign_container(empty_container):
    container = create_sign_container()
    assert container == empty_container


def test_get_sign_location_from_user(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    location = get_sign_location_from_user()
    assert location == 3


def test_assign_sign(monkeypatch, x_in_3_board, one_sign_container):
    monkeypatch.setattr('builtins.input', lambda _: '3')
    container = create_sign_container()
    board = assign_sign('X', container)
    assert board == x_in_3_board
    assert container == one_sign_container


def test_update_board(one_sign_container, x_in_3_board):
    board = update_board(one_sign_container)
    assert board == x_in_3_board

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
