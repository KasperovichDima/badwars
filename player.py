"""Player model."""
from protocols import Damageble, Weapon


class Player:
    """Representation of player on a game field."""

    def __init__(self, nickname: str, weapon: Weapon) -> None:
        """Player initializer."""
        self.nickname = nickname
        self._weapon = weapon
        self._hp = 20  # FIXME: Magic number!

    def make_damage(self, damageble_object: Damageble) -> None:
        """Hit some damageble object using self weapon.

        Runes can be applied here.
        """
        self._weapon.hit(damageble_object)

    def get_damage(self, damage: int) -> None:
        """Get damage from other player.

        Runes can be applied here.
        """
        self._hp -= damage
