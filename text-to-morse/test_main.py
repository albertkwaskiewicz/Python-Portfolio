import pytest
import main


def test_prompt_user(monkeypatch):
    monkeypatch.setattr('main.prompt_user', lambda: 'Hi')
    user_input = main.prompt_user()
    assert user_input == 'Hi'


def test_convert_user_input(monkeypatch):
    monkeypatch.setattr('main.prompt_user', lambda: 'Hi 74$ you@1')
    user_input = main.prompt_user()
    morse = main.convert_user_input(user_input)
    assert morse == '••••_•• --•••_••••- -•--_---_••- •----'


def test_clean_input_is_lowercase(monkeypatch):
    monkeypatch.setattr('main.prompt_user', lambda: 'Hi')
    user_input = main.prompt_user()
    user_input = main.clean_input(user_input)
    assert user_input == 'hi'


def test_clean_input_no_special_chars(monkeypatch):
    monkeypatch.setattr('main.prompt_user', lambda: 'Hello%#! World!34')
    user_input = main.prompt_user()
    user_input = main.clean_input(user_input)
    assert user_input == 'hello world 34'
