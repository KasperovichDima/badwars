"""Chests module. Contains all chasts logic."""
from random import choice
from typing import Literal

from runes import get_random_rune

class BaseChest:

    level: Literal[1, 2, 3]

    _is_exhausted = False

    def open(self):
        if not self._is_exhausted:
            self._is_exhausted = True
            self._perform_final_action()
            return get_random_rune(self.level)

        print('Sorry, I am exhausted...')

    def _perform_final_action(self):
        print('Do you want to buy me again bro?')


class GoldChest(BaseChest):
    """
    При открытии из этого сундука выпадает рандомная руна 1 или 2 уровня.
    """
    def __init__(self) -> None:
        self.level = choice((1, 2))


class DiamondChest(BaseChest):
    """При открытии из этого сундука выпадает рандомная руна 3 уровня."""

    level = 3


g = GoldChest()
print(g.open())
d = DiamondChest()
print(d.open())
