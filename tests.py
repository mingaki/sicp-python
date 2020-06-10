from math import pi

from abstract_numbers import ComplexMA, ComplexRI


def test_complex_add():
    ma = ComplexMA(2, 0.5 * pi)
    ri = ComplexRI(1, -1)
    s = ma + ri


def test_complex_mul():
    ma = ComplexMA(2, 0.5 * pi)
    ri = ComplexRI(1, 1)
    m = ma * ri
    assert m.magnitude == 2 * 2**0.5 and m.angle == 0.75 * pi, f"{m.magnitude}, {m.angle}"
