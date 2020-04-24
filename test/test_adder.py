import pytest

from module1.adder import Adder


@pytest.mark.set1
def test_add_num():
    a = 1
    b = 1
    assert Adder.add_num(a, b) == 2, "Custom fail message"


@pytest.mark.set2
def test_add_str():
    a = "abc"
    b = "def"
    assert Adder.add_str(a, b) == "abcdef"


@pytest.mark.set1
@pytest.mark.parametrize("a, b, r", [(1, 9, 10), (2, 8, 10), (3, 7, 10)])
def test_add_params(a, b, r):
    assert Adder.add_num(a, b) == r


@pytest.mark.skip
def test_skip1():
    assert Adder.add_num(1, 1) == 3, "Will never work"


@pytest.mark.xfail
def test_fail1():
    assert Adder.add_num(2, 2) == 5, "Nope"
