# tests/test_devider.py
import pytest

from arithmetics.devider import (
    devide_numbers
)

def test_devide_numbers():
    assert devide_numbers(1, 2) == 0.5
    assert devide_numbers(-1, 1) == -1
    assert devide_numbers(10, -5) == -2

def test_devide_zero():
    with pytest.raises(ZeroDivisionError):
        devide_numbers(1, 0)