from funcaoTeste import *
from funcaoWlad import *

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def test_subtract():
    assert subtract(2, 3) == -1
    
def test_subtract_2():
    numero = subtract (4,2)
    assert numero == 2
    funcaoWlad(numero)
    assert numero == 4
