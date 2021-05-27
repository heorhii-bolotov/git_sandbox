import pytest


@pytest.fixture
def innermost(order):
    order.append("innermost top")


def test_order(order, top):
    assert order == ["innermost top", "top"]


def test_top(order, innermost):
    assert order == ["innermost top"]
