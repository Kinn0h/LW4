import math
import unittest

class CircleTestCase(unittest.TestCase):

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_1(self):
        res = perimeter(8 * 105)
        self.assertEqual(res, math.pi * (8 * 105) * 2)

    def test_circle_perimeter_2(self):
        res = perimeter(450)
        self.assertEqual(res, math.pi * 450 * 2)


    def test_circle_area_1(self):
        res = area(10)
        self.assertEqual(res, math.pi * 100)

    def test_circle_area_2(self):
        res = area(7)
        self.assertEqual(res, math.pi * 7 ** 2)

    def test_circle_area_3(self):
        res = area(70)
        self.assertEqual(res, math.pi * 70 ** 2)

    def test_circle_area_4(self):
        res = area(27)
        self.assertEqual(res, math.pi * 27 ** 2 )


def area(r):
    return math.pi * r * r

def perimeter(r):
    return 2 * math.pi * r

