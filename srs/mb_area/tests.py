from math import pi
import unittest

from figures import Circle, Triangle


class CircleTestCase(unittest.TestCase):
    """Тест класса Circle."""

    def setUp(self) -> None:
        self.circle = Circle(2)

    def test_positive(self):
        """Проверка правильности работы атрибута и свойства класса."""

        right_area = 2 * pi * self.circle.radius ** 2

        self.assertEqual(self.circle.radius, 2)
        self.assertEqual(self.circle.area, right_area)

    def test_incorrect_radius(self):
        """Проверка невозможности создания класса с некорректным радиусом."""

        try:
            circle = Circle(-1)
            self.assertFalse(circle, msg='Круг не должен создаваться с некорректным радиусом')
        except Exception as error:
            self.assertIsInstance(error, ValueError)


class TriangleTestCase(unittest.TestCase):
    """Тест класса Triangle."""

    def setUp(self) -> None:
        self.ordinary_triangle = Triangle(8, 5, 5)
        self.isosceles_triangle = Triangle(6, 5)
        self.equilateral_triangle = Triangle(6)
        self.right_triangle = Triangle(3, 4, 5)

    def test_positive(self):
        """Проверка правильности работы атрибута и свойства класса."""

        right_area_ordinary = 12.0
        right_area_isosceles = 12.0
        right_area_equilateral = 15.58845726

        self.assertEqual(self.ordinary_triangle.area, right_area_ordinary)
        self.assertEqual(self.isosceles_triangle.area, right_area_isosceles)
        self.assertAlmostEqual(self.equilateral_triangle.area, right_area_equilateral)
        self.assertFalse(self.ordinary_triangle.is_right)
        self.assertTrue(self.right_triangle.is_right)

    def test_incorrect_sides(self):
        """Проверка невозможности создания класса с некорректными сторонами."""

        try:
            triangle = Triangle(8, 5, -5)
            self.assertFalse(triangle, msg='Треугольник не должен создаваться с отрицательными сторонами')
        except Exception as error:
            self.assertIsInstance(error, ValueError)
        try:
            triangle = Triangle(20, 1, 1)
            self.assertFalse(triangle, msg='Треугольник не должен создаваться с некорректными сторонами')
        except Exception as error:
            self.assertIsInstance(error, ValueError)


if __name__ == '__main__':
    unittest.main()
