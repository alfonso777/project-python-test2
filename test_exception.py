# content of test_sysexit.py
import pytest


def divide(x, y):
    return x/y


def test_mytest():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)