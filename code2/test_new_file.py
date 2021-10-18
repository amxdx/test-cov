from new_file import ToyExample
import pytest 

@pytest.fixture(scope = "module")
def te():
    toyex = ToyExample()
    return toyex

def test_useless_code_1(te):
    assert(te.useless_code_1() == None)

def test_useless_code_2(te):
    assert(te.useless_code_2() == None)