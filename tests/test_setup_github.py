import pytest
from download import setup_github

# libraries to overwrite
import click
import getpass


# NOTE: Github constructor doesn't check valid credentials, so this functionality
# did not have to be replaced with a mock. It should at some point
@pytest.fixture(autouse=True)
def test_patch_input(monkeypatch):
    """monkey patch all user input for all tests"""
    monkeypatch.setattr(click, 'prompt', lambda input, type: "foo")
    monkeypatch.setattr(getpass, 'getpass', lambda input: "bar")


def test_setup_github_config():
    """test when a config file is passed to via command line"""
    config = './tests/good-config.json'
    g = setup_github(None, None, None, config)
    assert g


def test_setup_github_bad_config():
    """test when a config file has nothing in it"""
    config = './tests/bad-config.json'
    g = setup_github(None, None, None, config)
    assert g


def test_setup_github_prompt():
    """test when nothing is passed via command line"""

    g = setup_github(None, None, None, None)
    assert g


def test_setup_github_username():
    """test when nothing is passed via command line"""

    g = setup_github('foo', None, None, None)
    assert g


def test_setup_github_password():
    """test when nothing is passed via command line"""

    g = setup_github(None, 'bar', None, None)
    assert g


def test_setup_github_username_password():
    """test when nothing is passed via command line"""

    g = setup_github('foo', 'bar', None, None)
    assert g


def test_setup_github_username_token():
    """test when nothing is passed via command line"""

    g = setup_github(None, None, 'token', None)
    assert g
