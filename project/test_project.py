import pytest
from project import add, sub, mult, div

def test_add():

    assert add(5, 5) == 10
    assert add(10, 4) == 14

    with pytest.raises("ValueError"):

        add('b', 5)

def test_sub():

    assert sub(20, 8) == 12
    assert sub(3, 1) == 2

    with pytest.raises("ValueError"):

        sub('g', 4)

def test_mult():

    assert mult(4, 4) == 16
    assert mult(2, 2) == 4

    with pytest.raises("ValueError"):

        mult(5, 'e')

def test_div():

    assert div(30, 10) == 3
    assert div(25, 5) == 5

    with pytest.raises("ZeroDivisionError"):

        div(9, 0)

    with pytest.raises("ValueError"):

        div(8, 't')



