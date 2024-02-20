# tests/test_adder.py
import pytest

from arithmetics.adder import (
    add_numbers
)

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(10, -5) == 5

def test_add_strings():
    with pytest.raises(ValueError):
        add_numbers("a", "b")