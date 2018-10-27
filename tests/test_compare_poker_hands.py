import pytest


def test_should_autofail():
    pytest.fail('You configured \"setup.py\" correctly, hooray!')

