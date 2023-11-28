"""Player model."""
import logging
from typing import cast

from enums import InventoryItemType
from protocols import (
    Damageble,
    InventoryItem,
    InventoryProto,
    Rune,
    WeaponProto,
)
from settings import MAX_HP_LEVEL


class Player:
    """Representation of player on a game field."""

    def __init__(
            self,
            nickname: str,
            weapon: WeaponProto,
            inventory: InventoryProto,
    ) -> None:
        """Player initializer."""
        self.nickname = nickname
        self._weapon = weapon
        self._inventory = inventory
        self._hp = MAX_HP_LEVEL

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

    def pick_up_item(self, item: InventoryItem) -> None:
        """Put some item to inventory."""
        self._inventory.add_item(item)

    def _apply_rune(self, rune_name: str, param: int) -> int:
        """Aplly specified rune to specified parameter."""
        runes = cast(
            list[Rune],
            self._inventory.show_items_by_type(InventoryItemType.RUNE)
        )
        for r in runes:
            if r.__class__.__name__ is rune_name:
                logging.info(f'{rune_name} was found! Applying!')
                return r.appply(param)
        logging.info(f'No {rune_name} was found...')
        return param
