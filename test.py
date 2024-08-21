import unittest
import libcplx as lc
import math
class TestLibcplx(unittest.TestCase):

    def test_suma(self):
        suma = lc.suma((5,9),(8,6))
        self.assertAlmostEqual(suma[0], 13)
        self.assertAlmostEqual(suma[1], 15)
        suma = lc.suma((8,2.5), (3.8, -5))
        self.assertAlmostEqual(suma[0], 11.8)
        self.assertAlmostEqual(suma[1], -2.5)

    def test_producto(self):
        producto = lc.producto((9,4),(4,8))
        self.assertAlmostEqual(producto[0], 4)
        self.assertAlmostEqual(producto[1], 88)
        producto = lc.producto((8,2.5), (3.8, -5))
        self.assertAlmostEqual(producto[0], 42.9)
        self.assertAlmostEqual(producto[1], -30.5)

    def test_resta(self):
        resta = lc.resta((9,4),(4,8))
        self.assertAlmostEqual(resta[0], 5)
        self.assertAlmostEqual(resta[1], -4)
        resta = lc.resta((8,2.5), (3.8, -5))
        self.assertAlmostEqual(resta[0], 4.2)
        self.assertAlmostEqual(resta[1], 7.5)

    def test_division(self):
        division = lc.division((9,4),(4,8))
        self.assertAlmostEqual(division[0],0.85)
        self.assertAlmostEqual(division[1], -0.7)
        division = lc.division((8,2.5), (3.8, -5))
        self.assertAlmostEqual(division[0], 0.4538539553752535)
        self.assertAlmostEqual(division[1], 1.2550709939148075)

    def test_modulo(self):
        self.assertAlmostEqual(lc.modulo((9,4)), (97 ** (1/2)))
        self.assertAlmostEqual(lc.modulo((3.8, -5)), (39.44 ** (1/2)))

    def test_conjugado(self):
        self.assertAlmostEqual(lc.conjugado((9,4)), (9,-4))
        self.assertAlmostEqual(lc.conjugado((3.8, -5)), (3.8, 5))

    def test_fase(self):
        self.assertAlmostEqual(lc.fase((9,4)),math.atan(4/9) )
        self.assertAlmostEqual(lc.fase((3.8, -5)), math.atan(-5/3.8))

    def test_cartesiano_a_polar(self):
        c_p = lc.cartesiano_a_polar((9,4))
        self.assertAlmostEqual(c_p[0], 9.848857801796104 )
        self.assertAlmostEqual(c_p[1], math.atan(4/9))
        c_p = lc.cartesiano_a_polar((3.8, -5))
        self.assertAlmostEqual(c_p[0], 6.2801273872430325)
        self.assertAlmostEqual(c_p[1], math.atan(-5/3.8))

    def test_polar_a_cartesiano(self):
        p_c = lc.polar_a_cartesiano((2,4.6))
        self.assertAlmostEqual(p_c[0], -0.22430505387010974)
        self.assertAlmostEqual(p_c[1], -1.9873820072669288)
        p_c = lc.polar_a_cartesiano((-5, 1))
        self.assertAlmostEqual(p_c[0], -2.701511529340699)
        self.assertAlmostEqual(p_c[1], -4.207354924039483)


if __name__ == '__main__':
    unittest.main()