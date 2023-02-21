from operations import add,sub,mul,div
import pytest

def test_1():
    assert add(88,22) == 110

def test_2():
    assert sub(34,21) ==13

def test_3():
    assert mul(45,26) == 1170

def test_4():
    assert mul(45,0) == 0

def test_5():
    assert div(450,10) == 45

def test_6():
    with pytest.raises(ZeroDivisionError) as e:
        result = div(342,0)
    assert isinstance(e.value,ZeroDivisionError)

def test_7():
    assert div(0,11) == 0

def test_8():
    assert sub(-9,-6) == -3

def test_9():
    assert mul(-3,-6) == 18

def test_10():
    assert add(24,0) == 24



