from typing import Protocol

from protocols import InventoryItem


result = {
    'Алмазный мечь': 120,
    'Деревянный щит': 50,
    'Шерстяной блок': 150,
    'Бронированная кровать': 1563,
}

class Money(Protocol): ...


class GameShop(Protocol):

    def sell(self, item: InventoryItem) -> Money: ...
    def inspect(self) -> dict[str, int]: ...
    def buy(self, item_to_buy: str) -> InventoryItem: ...
