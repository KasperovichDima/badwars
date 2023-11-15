"""Runes module. Contains all runes logic."""

from random import choice
from typing import Literal


class BaseRune:
    """Base rune class to inherit from."""

    def __init__(self, level: Literal[1, 2, 3]) -> None:
        """Initialize rune with specified level."""
        self._level = level

    def __repr__(self) -> str:
        """Get rune text representation."""
        return f'<{self.__class__.__name__} level: {self._level}>'


class RuneVp(BaseRune):
    """Vampire rune.

    Increase player's hp on self level's value when
    hitting an enemy. But no more than maximum hp level.
    """

    def add_hp(self, hp: int) -> int:
        """Increase player's hp on self level value.

        But no more than maximum hp level.
        """
        return min(hp + self._level, 20)  # FIXME: Magic number!


class RunePr(BaseRune):
    """Protection rune.

    Decrease received damage.
    """

    def reduce_damage(self, damage: int) -> int:
        """Decrease received damage on self level value.

        Damage can not be < 0.
        """
        return max(damage - self._level, 0)


class RuneAc(BaseRune):
    """Acura rune.

    When killing an enemy, restores the character's health to maximum with
    certain chance. This cance depends on rune level:
    * level 1 - 25%
    * level 2 - 50%
    * level 3 - 75%
    """

    def restore_hp(self, hp: int) -> int:
        """Restore player's hp to maximum level with certain chance."""
        chanses = [False] * 4
        for ind in range(self._level):
            chanses[ind] = True
        if choice(chanses):  # noqa: S311
            return 20  # FIXME: Magic number!
        return hp


def get_random_rune(level: Literal[1, 2, 3]):  # TODO: add return type
    """Return random rune of specified level."""
    rune_class = choice((RuneVp, RunePr, RuneAc))  # noqa: S311  TODO: change to __subclasses__
    return  rune_class(level)
