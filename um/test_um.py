import pytest
from um import count

def test_input():

    assert count("Um, thanks for the cd.") == 1
    assert count("um") == 1
    assert count("Um, thanks, um, yeah") == 2
    assert count("Um?") == 1