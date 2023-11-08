"""
TODO list:
1. Сделать классы рун. - Done!
2. Сделать классы сундуков, из которых эти руны будут выпадать. - Homework!
3. Рефакторинг - если успеем. - Done!
4. Сделать класс персонажа.

Разные типы оружия наносят разный урон разным блокам.
"""
from __future__ import annotations
from enum import Enum
from random import choice
from typing import Literal, Protocol


class BaseRune:
    def __init__(self, level: Literal[1, 2, 3]) -> None:
        self._level = level


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


class GoldChest:
    """
    При открытии из этого сундука выпадает рандомная руна 1 или 2 уровня.
    """

    def open(self):
        """Создает и возвращает рандомную руну 1 или 2 уровня."""


class DiamondChest:
    """При открытии из этого сундука выпадает рандомная руна 3 уровня."""

    def open(self):
        """Создает и возвращает рандомную руну 3 уровня."""


class SwordType(Enum):
    """Sword type and sword damage"""
    WoodSword = 3
    IronSword = 4
    GoldenSword = 5
    DiamondSword = 7


# class Bed:
#     def __init__(self) -> None:
#         self._hp = 40

#     def get_damage(self, damage: int) -> None:
#         self._hp -= damage


# class Block:
#     def __init__(self) -> None:
#         self._hp = 10

#     def get_damage(self, damage: int) -> None:
#         self._hp -= damage


class Sword:
    def __init__(self, sword_type: SwordType) -> None:
        self._name = sword_type.name
        self._damage = sword_type.value

    def hit(self, damage_object: Damageble) -> None:
        damage_object.get_damage(self._damage)


class Damageble(Protocol):

    def get_damage(self, damage: int) -> None: ...


class Player:

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self._hp = 20
        self._weapon = Sword(SwordType.WoodSword)

    def make_damage(self, damage_object: Damageble) -> None:
        self._weapon.hit(damage_object)

    def get_damage(self, damage: int) -> None:
        self._hp -= damage
