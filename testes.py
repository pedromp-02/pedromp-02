from funcaoTeste import *

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def test_subtract():
    assert subtract(2, 3) == -1
    
def test_subtract_2():
    assert subtract(5, 3) == 2
