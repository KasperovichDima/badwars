"""Game protocols."""
from typing import Protocol


class Damageble(Protocol):
    """Any instance that can get damage."""

    def get_damage(self, damage: int) -> None:
        """Get and apply damage."""


class Weapon(Protocol):
    """Any weapon that can hit damagebel object."""

    def hit(self, damage_object: Damageble) -> None:
        """Apply self damage to damageble object."""
