from funcaoTeste import *

def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    
def test_subtract():
    assert subtract(2, 3) == -1
