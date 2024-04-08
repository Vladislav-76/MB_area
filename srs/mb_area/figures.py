from base import BaseFlatFigure
from math import pi


class Circle(BaseFlatFigure):
    """
    Класс круга.
    
    - radius: float - радиус круга, обязательный атрибут.
    """

    name = 'Круг'

    def __init__(self, radius: float) -> None:
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

    def __init__(self, a: float, b: float | None = None, c: float | None = None) -> None:
        self.a = a
        self.b = b if b else a
        self.c = c if c else self.b
        p = (self.a + self.b + self.c) / 2
        if (x := (p - self.a) * (p - self.b) * (p - self.c)) < 0:
            raise ValueError('Треугольника с такими сторонами быть не может.')
        super().__init__(p=p, x=x, area_calc=self.area_calc)

    @staticmethod
    def area_calc(p: float, x: float) -> float:
        """Функция вычисления площади."""

        return (p * x) ** 0.5
        
    @property
    def is_right(self) -> bool:
        sides = sorted((self.a, self.b, self.c))
        return sides.pop() ** 2 == sides.pop() ** 2 + sides.pop() ** 2




cir = Circle(1)
print(cir.area)
print(cir.radius)
tri = Triangle(10, 9)
print(tri.area)
print(tri.is_right)
tri = (Triangle(3, 4, 5))
print(tri.area)
print(tri.is_right)
Triangle(20, 4, 5)
