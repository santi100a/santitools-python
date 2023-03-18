import santitools.math as smath

def test_sqrt():
    assert smath.sqrt(65_536) == 256
    assert smath.sqrt(256) == 16
    assert smath.sqrt(16) == 4
    assert smath.sqrt(4) == 2

    assert smath.sqrt(625) == 25
    assert smath.sqrt(25) == 5
def test_invert():
    assert smath.invert(1) == 1
    assert smath.invert(2) == 0.5 # 1 / 2
    assert smath.invert(3) == 0.3333333333333333 # 1 / 3
    assert smath.invert(4) == 0.25 # 1 / 4
    assert smath.invert(4/3) == 0.75 # 3 / 4
def test_pendants_equation():
    assert smath.pendants_equation(5, -3, 8, 4) == 2.3333333333333335 # 7 / 3
