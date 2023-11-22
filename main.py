"""Main game module.

TODO list:
* Сделать классы рун. - Done!
* Сделать классы сундуков, из которых эти руны будут выпадать. - Done!
* Рефакторинг - если успеем. - Done!
* Сделать класс персонажа. - Done!
* Разобрать дз. - Done!
* Разнести все по каталогам. - Done!
* Еще сильнее упростить сундуки. - Done!
* убрать магические числа. - Done!
* добавить __subclasses__ в get_randome_rune. - Done!
* Сделать чтобы алмазный сундук сожно было открыть только открыв 30 золотых. - Done!

* Разобрать домашку.
* Сделать инвентарь.
    * добавить типы для каждого предмета
    * создать класс инвентаря
    * сделать добавление в инвентарь
    * сделать получение предмета из инвентаря


* Сделать применение рун.

Вопросы:
Марк: Что такое .gitignore? - Done!
Клим: Как работать с логами.


Разные типы оружия наносят разный урон разным блокам.
"""  # noqa: E501
import logging

from chests import GoldChest
from player import Player
from weapons import Sword, SwordType

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def create_new_player(nickname: str) -> Player:
    """Create new player on game map."""
    new_player_weapon = Sword(SwordType.WoodSword)
    return Player(nickname, new_player_weapon)


klim = create_new_player('Klim')
artem = create_new_player('Artem')
mark = create_new_player('Mark')
g = GoldChest()

rune = g.open('Dima')
