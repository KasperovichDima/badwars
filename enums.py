"""Game enums."""
from enum import Enum, auto


class SwordType(Enum):
    """Sword type and sword damage."""

    WoodSword = 3
    IronSword = 4
    GoldenSword = 5
    DiamondSword = 7


class InventoryItemType(Enum):
    """Types of item that can be added to inventory."""

    WEAPON = auto()
    RUNE = auto()
