"""Runes module. Contains all rune logic."""

from random import choice
from typing import Literal


class BaseRune:
    def __init__(self, level: Literal[1, 2, 3]) -> None:
        self._level = level

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} level: {self._level}>'


class RuneVp(BaseRune):
    """
    Руна вампирка.
    При ее применении увеличивает здоровье персонажа
    на уровень руны, когда наносится урон врагу.
    Но не больше максимума.
    """
    def add_hp(self, hp: int) -> int:
        """
        Этот метод принимает здороье персонажа, увеличивает
        его на уровень руны и возвращает назад.
        """
        return min(hp + self._level, 20)


class RunePr(BaseRune):
    """
    Руна защиты.
    Снижает получаемый персонажем урон на уровень руны.
    """
    def reduce_damage(self, damage: int) -> int:
        """
        Принимает урон (целое число), уменьшает
        его на уровень руны и возвращает назад.
        """
        return max(damage - self._level, 0)


class RuneAc(BaseRune):
    """
    Руна Акура.
    При убийстве противника восстанавливает здоровье персонажа до максимума
    с определенным шансом. Этот шанс зависит от уровня руны.
    1 уровень - 25%
    2 уровень - 50%
    3 уровень - 75%
    """
    def restore_hp(self, hp: int) -> int:
        chanses = [False] * 4
        for ind in range(self._level):
            chanses[ind] = True
        if choice(chanses):
            return 20
        return hp


def get_random_rune(level: Literal[1, 2, 3]):  # TODO: add return type
    """Return random rune of specified level."""
    rune_class = choice((RuneVp, RunePr, RuneAc))
    return  rune_class(level)
