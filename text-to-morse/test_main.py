import pytest
import main


def test_prompt_user(monkeypatch):
    monkeypatch.setattr('main.prompt_user', lambda: 'Hi')
    user_input = main.prompt_user()
    assert user_input == 'Hi'


