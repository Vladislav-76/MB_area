from abc import ABC, abstractmethod


class BaseFlatFigure(ABC):
    """
    Базовый класс плоской фигуры.

    - name: str - название фигуры, переопределяется для конкретной фигуры,
    - area_calc - функция вычисления площади конкретной фигуры,
    - kwargs - аргументы функции area_calc,
    - area:float - свойство возвращающее площадь.
    """

    def __init__(self, area_calc: callable, **kwargs) -> None:
        self._area = area_calc(**kwargs)

    name: str = 'BaseFigure'

    @property
    def area(self) -> float:
        """Площадь фигуры."""

        return float(self._area)
