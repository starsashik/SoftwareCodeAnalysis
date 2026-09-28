import pytest

from Calculator import Calculator

calculator = Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (10, 5, 15),
        (-2, 5, 3),
        (0, 0, 0),
        (1.5, 2.5, 4.0),
    ]
)
def test_add(a, b, expected):
    assert calculator.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 3, 7),
        (5, 8, -3),
        (0, 5, -5),
        (-5, -2, -3),
    ]
)
def test_subtract(a, b, expected):
    assert calculator.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (5, 0, 0),
        (-2, 4, -8),
        (1.5, 2, 3.0),
    ]
)
def test_multiply(a, b, expected):
    assert calculator.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (5, 2, 2.5),
        (-10, 2, -5),
        (0, 5, 0),
    ]
)
def test_divide(a, b, expected):
    assert calculator.divide(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        calculator.divide(10, 0)


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),

        (1, False),
        (4, False),
        (8, False),
        (9, False),
        (15, False),
        (-3, False),
    ]
)
def test_is_prime_number(number, expected):
    assert calculator.is_prime_number(number) == expected
