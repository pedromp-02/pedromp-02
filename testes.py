from funcaoTeste import *
from funcaoWlad import *
from pastaTeste.funcaoTeste import *

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def test_subtract():
    assert subtract(2, 3) == -1
    
def test_subtract_2():
    numero = subtract (4,2)
    assert numero == 2
    numero = funcaoWlad(numero)
    assert numero ==4
    
def testeWlad():
    numero = funcaoWlad(2)
    assert numero == 4

def testePasta():
    numero = soma2(2)
    assert numero == 4
