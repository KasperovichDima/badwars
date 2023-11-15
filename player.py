"""Player model."""
from protocols import Damageble, Weapon


class Player:

    def __init__(self, nickname: str, weapon: Weapon) -> None:
        self.nickname = nickname
        self._hp = 20
        self._weapon = weapon

    def make_damage(self, damage_object: Damageble) -> None:
        self._weapon.hit(damage_object)

    def get_damage(self, damage: int) -> None:
        self._hp -= damage
