import pytest


def f():
    return 3


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
    with pytest.raises(IOError):
        pass


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert "maximum recursion" in str(excinfo.value)