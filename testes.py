import funcaoTeste
def test_add():
    assert add(2, 2) == 5
    assert add('space', 'ship') == 'spaceship'
    
def test_subtract():
    assert subtract(2, 3) == -1
