"""Chests module. Contains all chasts logic."""
import logging
from collections import defaultdict
from random import choice
from typing import Literal

from runes import get_random_rune
from settings import MIN_CHESTS_OPENING


class BaseChest:
    """Base chest class for inheritance."""

    level: Literal[1, 2, 3]

    _is_exhausted = False

    _openings_by_player: dict[str, int] = defaultdict(int)

    def open_chest(self, nickname: str):
        """Open chest and get random rune of chest level."""
        if self._is_exhausted:
            logging.warning('Sorry, I am exhausted...')
            return
        self._openings_by_player[nickname] += 1
        self._is_exhausted = True
        self._perform_final_action()
        return get_random_rune(self.level)


    def _perform_final_action(self) -> None:
        logging.info('Do you want to buy me again bro?')


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

    def open_chest(self, nickname: str):
        if self._openings_by_player[nickname] >= MIN_CHESTS_OPENING:
            return super().open_chest(nickname)
        gold_to_open = MIN_CHESTS_OPENING - self._openings_by_player[nickname]
        logging.info(f'You have to open {gold_to_open} gold chests first!')

    level = 3
