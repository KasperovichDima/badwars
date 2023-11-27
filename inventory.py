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
        self._items[item.item_type].append(item)

    # def take_item(self, item_type: InventoryItemType, item_ind: int) -> InventoryItem:  # noqa: E501
    #     """Return specified item from inventory."""

    def __repr__(self) -> str:
        for 

    @property
    def invenory_size(self) -> int:
        """Number of items in inventory."""
        # invenory_size = 0
        # for item_list in self._items.values():
        #     invenory_size += len(item_list)
        # return invenory_size
        return sum(len(items) for items in self._items.values())

    @property
    def _is_full(self) -> bool:
        return self.invenory_size == MAX_INVENTORY_SIZE
