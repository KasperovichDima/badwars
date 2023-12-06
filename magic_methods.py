"""Useful magic methods.

__init__ *
__repr__ *
__del__ *
__add__ +
__sub__ -
__eq__ ==
__lt__ <
__gt__ >
__le__ <=
__ge__ >=
__bool__

__in__
__getitem__
__setitem__
__next__
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
        money_type = self.type
        new_value = self.value + other.value
        return money_class(money_type, new_value)

    def __sub__(self, other: Self) -> Self:
        """Отнять от этих денег другие деньги и получить новые."""
        if self.type is not other.type:
            raise TypeError(f'Can not sub {other.type.name} from {self.type.name}!')

        money_class = self.__class__
        money_type = self.type
        new_value = self.value - other.value
        return money_class(money_type, new_value)

    def __eq__(self, other: Self) -> bool:
        """Check if other money object is the same."""
        return all((
            self.type == other.type,
            self.value == other.value
        ))

    def __gt__(self, other: Self) -> bool:
        """Check if this money are greater than other."""
        if self.type is not other.type:
            raise TypeError(f'Can not compare {other.type.name} with {self.type.name}!')
        return self.value > other.value

    def __repr__(self) -> str:
        return f'<{self.type.name}: {self.value}>'


# m1 = Money(MoneyType.Gold, 120)
# print(m1)
# m2 = Money(MoneyType.Gold, 30)
# print(m2)
# m3 = m1 - m2
# print(m3)


assert Money(MoneyType.Gold, 120) - Money(MoneyType.Gold, 30) == Money(MoneyType.Gold, 90)
assert Money(MoneyType.Gold, 120) > Money(MoneyType.Gold, 30)
print('TESTS PASSED!')


class Wallet:

    def __init__(self) -> None:
        self._banknotes: list[int] = []

    def add_money(self, money: int) -> None:
        self._banknotes.append(money)

    def take_last_banknote(self) -> int | None:
        try:
            return self._banknotes.pop()
        except IndexError:
            return None

    def __bool__(self) -> bool:
        """Check if wallet is not empty.

        True - if some money in wallet. Else - False.
        """
        return bool(self._banknotes)

    def __in__(self, value: int) -> bool:
        return value in self._banknotes


wallet = Wallet()
wallet.add_money(10)

if 5 in wallet:
    print('Да, держи пятерку!')
