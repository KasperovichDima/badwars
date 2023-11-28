"""Player's inventory."""
import logging
from collections import defaultdict

from enums import InventoryItemType
from protocols import InventoryItem
from settings import MAX_INVENTORY_SIZE


class Inventory:

    def __init__(self) -> None:
        """Inventory init."""
        self._items: dict[InventoryItemType, list[InventoryItem]] = defaultdict(list)

    def add_item(self, item: InventoryItem) -> None:
        """Add item to inventory.

        If inventory is full - item will not be added.
        """
        if self._is_full:
            logging.error('Inventory is full! Item will not be added!')
            return
        self._items[item.item_type].append(item)

    def show_items_by_type(
            self,
            target_type: InventoryItemType
    ) -> tuple[InventoryItem, ...]:
        """Show all items of specified type in inventory."""
        return tuple(self._items[target_type])

    @property
    def _is_full(self) -> bool:
        return len(self) == MAX_INVENTORY_SIZE

    def __len__(self) -> int:
        """Count elements in inventory."""
        return sum(len(items) for items in self._items.values())
