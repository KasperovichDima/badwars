"""Game protocols."""
from typing import Protocol

from enums import InventoryItemType


class Damageble(Protocol):
    """Any instance that can get damage."""

    def get_damage(self, damage: int) -> None:
        """Get and apply damage."""


class WeaponProto(Protocol):
    """Any weapon that can hit damagebel object."""

    def hit(self, damage_object: Damageble) -> None:
        """Apply self damage to damageble object."""


class InventoryItem(Protocol):
    """Any item that can be added to inventory.

    Must have InventoryItemType.
    -
    """

    item_type: InventoryItemType


class InventoryProto(Protocol):
    """Inventory protocol."""

    def add_item(self, item: InventoryItem) -> None: ...
    def show_items_by_type(self, target_type: InventoryItemType) -> tuple[InventoryItem, ...]: ...  # noqa: E501
    def __len__(self) -> int: ...


class Rune(Protocol):
    """Rune protocol with apply method."""

    def appply(self, parametr: int) -> int: ...
