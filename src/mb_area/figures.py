from math import pi

from .base import BaseFlatFigure


class Circle(BaseFlatFigure):
    """
    Класс круга.

    - radius: float - радиус круга, обязательный атрибут.
    """

    name = 'Круг'

    def __init__(self, radius: int | float) -> None:
        if radius <= 0:
            raise ValueError('Радиус круга должен быть положительным числом')
        self.radius = radius
        super().__init__(radius=radius, area_calc=lambda radius: 2 * pi * radius ** 2)


class Triangle(BaseFlatFigure):
    """
    Класс треугольника.

    - a: float - сторона треугольника, обязательный аргумент,
    - b: float - сторона треугольника, если задается только сторона a, треугольник равносторонний,
    - c: float - сторона треугольника, если задаются только стороны a и b, треугольник равнобедренный с основанием a,
    - is_right: bool - проверка прямоугольности.
    """

    name = 'Треугольник'

    def __init__(self, a: int | float, b: int | float | None = None, c: int | float | None = None) -> None:
        self.a = a
        self.b = b if b else a
        self.c = c if c else self.b
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise ValueError('Стороны треугольника должны быть положительными числами')
        p = (self.a + self.b + self.c) / 2
        if (x := (p - self.a) * (p - self.b) * (p - self.c)) < 0:
            raise ValueError('Треугольника с такими сторонами быть не может')
        super().__init__(p=p, x=x, area_calc=self.area_calc)

    @staticmethod
    def area_calc(p: float, x: float) -> float:
        """Функция вычисления площади."""

        return (p * x) ** 0.5

    @property
    def is_right(self) -> bool:
        """Свойство проверки прямоугольности."""
        sides = sorted((self.a, self.b, self.c))
        return sides.pop() ** 2 == sides.pop() ** 2 + sides.pop() ** 2
