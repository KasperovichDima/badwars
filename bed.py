"""Bed class."""
from typing import Self

from settings import BED_HP


class Bed:
    """Кровать - основа команды.

    Условия:
    -
    можно сломать только:
    * Киркой
    * Топором
    * Ножницами

    При появлении кровать не защищена блоками.
    Отличаются цветами друг от друга.
    * BLUE
    * GREEN
    * RED
    * YELLOW

    Кровать хранит ссылки на объекты игроков
    своей команды. Если игрок умер - она его возраждает.
    """

    _hp = BED_HP

    def __init__(self, color: str) -> None:
        self.color = color

    def __eq__(self, other: Self) -> bool:
        if self.color == other.color and self._hp == other._hp:
            return True
        return False


def create_beds() -> list[Bed]:
    return [Bed(color) for color in 'BLUE GREEN RED YELLOW'.split()]


reference_result = [Bed('BLUE'), Bed('GREEN'), Bed('RED'), Bed('YELLOW')]
func_result = create_beds()

assert reference_result == func_result
print('TEST PASSED!')