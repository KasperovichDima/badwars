"""Weapons module. Describes all available weapon."""

from enum import Enum

from protocols import Damageble


class SwordType(Enum):
    """Sword type and sword damage"""
    WoodSword = 3
    IronSword = 4
    GoldenSword = 5
    DiamondSword = 7


class Sword:
    def __init__(self, sword_type: SwordType) -> None:
        self._name = sword_type.name
        self._damage = sword_type.value

    def hit(self, damage_object: Damageble) -> None:
        damage_object.get_damage(self._damage)
