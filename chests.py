"""Chests module. Contains all chasts logic."""
from random import choice
from typing import Literal

from runes import get_random_rune


class BaseChest:
    """Base chest class for inheritance."""

    level: Literal[1, 2, 3]

    _is_exhausted = False

    def open(self):
        """Open chest and get random rune of chest level."""
        if not self._is_exhausted:
            self._is_exhausted = True
            self._perform_final_action()
            return get_random_rune(self.level)

        print('Sorry, I am exhausted...')

    def _perform_final_action(self) -> None:
        print('Do you want to buy me again bro?')


class GoldChest(BaseChest):
    """Gold Chest class.

    Gives you random rune of level 1 or 2.
    """

    def __init__(self) -> None:
        """Choose rune level."""
        self.level = choice((1, 2))  # noqa: S311


class DiamondChest(BaseChest):
    """Gold Chest class.

    Gives you random rune of level 3.
    """

    level = 3


g = GoldChest()
print(g.open())
d = DiamondChest()
print(d.open())
