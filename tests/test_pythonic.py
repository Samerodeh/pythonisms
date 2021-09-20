from pythonic import __version__
from pythonic.pythonic import *
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def value():
  list = LinkedList()
  list.insert(3)
  list.insert(5)
  list.insert(1)
  return list

def test_list(value):
 assert len(value) == 3

def test_dunder_method_1(value):
    assert str(value) == "[1] -> [5] -> [3] -> None"
    
def test_dunder_method_2(value):
    assert value[1] == 5

def test_dunder_method_3(value):
    expected=[1,5,3]
    for idx, item in enumerate(value):
        assert item == expected[idx]