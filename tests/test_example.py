# tests/test_example.py

import pytest

# Тест на деление на ноль
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        x = 1 / 0

# Тест на чётность числа
def test_is_even():
    assert 4 % 2 == 0
    assert 7 % 2 != 0

# Тест на нечётность числа
def test_is_odd():
    assert 5 % 2 != 0
    assert 10 % 2 == 0
