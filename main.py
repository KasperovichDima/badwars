"""Main game module.

TODO list:
1. Сделать классы рун. - Done!
2. Сделать классы сундуков, из которых эти руны будут выпадать. - Done!
3. Рефакторинг - если успеем. - Done!
4. Сделать класс персонажа. - Done!
5. Разобрать дз. - Done!
6. Разнести все по каталогам. - Done!
7. Еще сильнее упростить сундуки. - Done!
8. Сделать применение рун.
9. Сделать инвентарь.

Вопросы: Марк: Что такое .gitignore?

Разные типы оружия наносят разный урон разным блокам.
"""

from player import Player
from weapons import Sword, SwordType


def create_new_player(nickname: str) -> Player:
    """Create new player on game map."""
    new_player_weapon = Sword(SwordType.WoodSword)
    return Player(nickname, new_player_weapon)


klim = create_new_player('Klim')
artem = create_new_player('Artem')
mark = create_new_player('Mark')
