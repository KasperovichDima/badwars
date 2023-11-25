"""Weapons module. Describes all available weapon."""
from enums import InventoryItemType, SwordType
from protocols import Damageble


class Sword:
    """Sword - milee weapon."""

    item_type = InventoryItemType.WEAPON

    def __init__(self, sword_type: SwordType) -> None:
        self._name = sword_type.name
        self._damage = sword_type.value

    def hit(self, damage_object: Damageble) -> None:
        damage_object.get_damage(self._damage)
