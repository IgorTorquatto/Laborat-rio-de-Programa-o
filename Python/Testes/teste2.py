def fatorial(n):
    if n < 0:
        return 0
    i=1
    fat=1
    while i <= n: # Testar primeiro com  i < n para ver os erros.
        fat = fat * i
        i=i+1
    return fat

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial10n():
    assert fatorial(-10) == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120