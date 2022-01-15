from monom import Monom

def test_constr():
    m = Monom(12)
    assert m[1] == 1
    assert m[2] == 1
    assert m[3] == 0
    assert m[4] == 0
    assert int(m) == 12
    assert m.nr1() == 2
    n = Monom([1, 0, 0, 0])
    p = m + n
    assert p.nivel_factorizare() == 1

def test():
    test_constr()
