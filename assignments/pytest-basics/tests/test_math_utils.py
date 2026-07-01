from math_utils import add, subtract, multiply, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_subtract_negative_result():
    assert subtract(2, 5) == -3


def test_multiply_by_zero():
    assert multiply(10, 0) == 0


def test_divide_by_nonzero():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises():
    try:
        divide(5, 0)
        assert False, "Expected ValueError"
    except ValueError:
        assert True
