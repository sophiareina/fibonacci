from fib import get_fib


def test_zero():
    assert get_fib(0) == 0

def test_one():
    assert get_fib(1) == 1

def test_two():
    assert get_fib(2) == 1

def test_ten():
    assert get_fib(10) == 55