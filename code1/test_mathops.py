import datetime
import pytest
import mathops

@pytest.fixture(scope ="module")
def Calc():
    from mathops import Calculator
    cal = Calculator()
    return cal
    
@pytest.fixture(scope ="module")
def Talk():
    from mathops import Talker
    talk = Talker()
    return talk

@pytest.mark.parametrize("a,b,result",
    [
        (1,2,3),
        (2,3,5),
        (4,5,9),
        (10,10,20),
        (400,-400,0)
    ]
    )
def test_add(Calc, a, b, result):
    assert (Calc.add(a,b) == result)

@pytest.mark.parametrize("a,b,result",
    [
        (1,2,2),
        (2,3,6),
        (4,5,20),
        (10,10,100),
        (400,-400,-160000)
    ]
    )
def test_multiply(Calc, a, b, result):
    assert (Calc.multiply(a,b) == result)

@pytest.mark.parametrize("a,b,result",
    [
        (1,2,0.5),
        (2,3,2/3),
        (4,5,0.8),
        (10,10,1),
        (400,-400,-1)
    ]
    )
def test_divide(Calc, a, b, result):
    assert (Calc.divide(a,b) == result)

def test_sayHello(Talk):
    assert (Talk.sayHello() == "Hello, how are you!")

@pytest.mark.parametrize("name, result",
    [
        ("Ashish", "Hello, how are you Ashish"),
        ("amxdx", "Hello, how are you amxdx"),
        ("AGAG", "Hello, how are you AGAG"),
    ]
    )
def test_sayHelloName(Talk, name, result):
    assert (Talk.sayHelloName(name) == result)

def test_date(Talk):
    assert (Talk.somedate() == datetime.date(2014,11,4))
