"""Useful magic methods.

__init__ *
__del__ *
__add__ *
__sub__
__str__
__repr__ *
__eq__
__lt__
__gt__
__le__
__ge__
__bool__
__in__
__getitem__
__setitem__
__iter__
__len__
"""
from enum import Enum, auto
from typing import Self


class MoneyType(Enum):

    Keys = auto()
    Gold = auto()
    Emeralds = auto()


class Money:

    def __init__(self, money_type: MoneyType, value: int) -> None:
        self.type = money_type
        self.value = value

    def __add__(self, other: Self) -> Self:
        """Add one unit of money to another one.

        Type of money must be the same.
        """
        if self.type is not other.type:
            raise TypeError(f'Can not add {other.type.name} to {self.type.name}!')

        money_class = self.__class__
        mone_type = self.type
        new_value = self.value + other.value
        return money_class(mone_type, new_value)

    def __repr__(self) -> str:
        return f'<{self.type.name}: {self.value}>'


m1 = Money(MoneyType.Gold, 120)
m2 = Money(MoneyType.Keys, 30)
m3 = m1 + m2
