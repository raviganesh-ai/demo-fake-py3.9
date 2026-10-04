import math

import calc


def test_add():
    assert calc.add(2, 3) == 5


def test_subtract():
    assert calc.subtract(5, 3) == 2


def test_multiply():
    assert calc.multiply(4, 3) == 12


def test_divide():
    assert calc.divide(10, 2) == 5


def test_divide_by_zero_raises():
    try:
        calc.divide(1, 0)
        assert False, "expected ZeroDivisionError"
    except ZeroDivisionError:
        pass


def test_factorial():
    assert calc.factorial(5) == 120


def test_is_prime():
    assert calc.is_prime(7) is True
    assert calc.is_prime(8) is False


def test_fibonacci():
    assert calc.fibonacci(10) == 55


def test_mean():
    assert calc.mean([1, 2, 3, 4]) == 2.5


def test_median_even():
    assert calc.median([1, 2, 3, 4]) == 2.5


def test_area_circle():
    assert math.isclose(calc.area_circle(2), math.pi * 4)


def test_celsius_to_fahrenheit():
    assert calc.celsius_to_fahrenheit(0) == 32


def test_is_perfect_square():
    assert calc.is_perfect_square(16) is True
    assert calc.is_perfect_square(15) is False


def test_clamp():
    assert calc.clamp(15, 0, 10) == 10
    assert calc.clamp(-5, 0, 10) == 0
    assert calc.clamp(5, 0, 10) == 5
