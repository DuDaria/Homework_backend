import unittest

from hw07_easy import Figure, IsoscelesTrapezoid, Triangle


class TestFigure(unittest.TestCase):
    name = "Тест"
    perim = 123
    sq = 123
    figure = Figure(name, perim, sq)

    def test_get_result(self): 
        self.assertRaises(TypeError, self.figure.get_result, None)
        self.assertIsInstance(self.figure.name, str)
        self.assertIsInstance(self.figure.perim, int)
        self.assertIsInstance(self.figure.sq, int)


class TestTriangle(unittest.TestCase):
    A = (3, 2)
    B = (1, 1)
    C = (1, 3)
    triangle = Triangle(A, B, C)

    def test_init(self):
        self.assertEqual((self.triangle.A, self.triangle.B, self.triangle.C), \
        ((3, 2), (1, 1), (1, 3)))
        
        for i in self.triangle.A or i in self.triangle.B \
        or i in self.triangle.C:
            self.assertIsInstance(i, int)
            self.assertEqual((i), (i))
            self.assertNotEqual(i, '')
            self.assertNotEqual(i, ' ')
            self.assertRaises(TypeError, i, None)
            self.assertRaises(TypeError, i, '123')
            self.assertRaises(TypeError, i, '')
            self.assertRaises(TypeError, i, ' ')   

    def test_get_name(self):
        self.assertEqual(self.triangle.get_name(), ('Треугольник'))
        self.assertTrue(self.triangle.get_name, True)
        self.assertRaises(TypeError, self.triangle.get_name, None)

    def test_perim_triang(self):
        self.assertRaises(TypeError, self.triangle.perim_triang, None)
        self.assertRaises(TypeError, self.triangle.perim_triang, '123')
        self.assertRaises(TypeError, self.triangle.perim_triang, '')
        self.assertRaises(TypeError, self.triangle.perim_triang, ' ')

    def test_square_triang(self):
        self.assertRaises(TypeError, self.triangle.square_triang, None)
        self.assertRaises(TypeError, self.triangle.square_triang, '123')
        self.assertRaises(TypeError, self.triangle.square_triang, '')
        self.assertRaises(TypeError, self.triangle.square_triang, ' ')

    def test_hight_triang(self):
        self.assertRaises(TypeError, self.triangle.hight_triang, None)
        self.assertRaises(TypeError, self.triangle.hight_triang, '123')
        self.assertRaises(TypeError, self.triangle.hight_triang, '')
        self.assertRaises(TypeError, self.triangle.hight_triang, ' ')


class TestIsoscelesTrapezoid(unittest.TestCase):
    A = (1, 1)
    B = (1, 5)
    C = (3, 4)
    D = (3, 2)
    trapezoid = IsoscelesTrapezoid(A, B, C, D)

    def test_init(self):
        for i in self.trapezoid.A or i in self.trapezoid.B \
        or i in self.trapezoid.C or i in self.trapezoid.D:
            self.assertIsInstance(i, int)
            self.assertEqual((i), (i))
            self.assertNotEqual(i, '')
            self.assertNotEqual(i, ' ')
            self.assertRaises(TypeError, i, None)
            self.assertRaises(TypeError, i, '123')
            self.assertRaises(TypeError, i, '')
            self.assertRaises(TypeError, i, ' ')       

    def test_get_side_len(self):
        self.assertRaises(TypeError, self.trapezoid.get_side_len, None)
        self.assertRaises(TypeError, self.trapezoid.get_side_len, '123')
        self.assertRaises(TypeError, self.trapezoid.get_side_len, '')
        self.assertRaises(TypeError, self.trapezoid.get_side_len, ' ')

    def test_get_name(self):
        self.assertEqual(self.trapezoid.get_name(), ("Равнобедренная трапеция"))
        self.assertTrue(self.trapezoid.get_name, True)
        self.assertRaises(TypeError, self.trapezoid.get_name, None)

    def test_perim_trap(self):
        self.assertRaises(TypeError, self.trapezoid.get_side_len, None)
        self.assertRaises(TypeError, self.trapezoid.get_side_len, '123')
        self.assertRaises(TypeError, self.trapezoid.get_side_len, '')
        self.assertRaises(TypeError, self.trapezoid.get_side_len, ' ')

    def test_square_trap(self):
        self.assertRaises(TypeError, self.trapezoid.get_side_len, None)
        self.assertRaises(TypeError, self.trapezoid.get_side_len, '123')
        self.assertRaises(TypeError, self.trapezoid.get_side_len, '')
        self.assertRaises(TypeError, self.trapezoid.get_side_len, ' ')



if __name__ == "__main__":
    unittest.main()
