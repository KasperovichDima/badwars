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

* Разобрать домашку. - Done!
* Кратко разобрать логи - Done!

* Сделать инвентарь.
    * создать класс инвентаря - Done!
    * сделать добавление в инвентарь - Done!
    * Сделать enums в отдельном файле - Done!
    * добавить типы для каждого предмета - Done!
    * сделать протокол для предмета - Done!
    * сделать протокол для руны - Done!
    * использовать магический метод len для размера инвентаря
    * сделать обзор инвентаря по категориям предметов
    * не забыть поменять интерфейс инвентаря!

* Разобраться с протоколами. - Done!
* Сделать применение рун.
* Разобраться с cast.

Вопросы:
Марк: Что такое .gitignore? - Done!
Клим: Как работать с логами. - Done!


Разные типы оружия наносят разный урон разным блокам.
"""  # noqa: E501
import logging

from inventory import Inventory
from player import Player
from weapons import Sword, SwordType

#  Logging config.
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def create_new_player(nickname: str) -> Player:
    """Create new player on game map."""
    new_player_weapon = Sword(SwordType.WoodSword)
    new_player_inventory = Inventory()
    return Player(nickname, new_player_weapon, new_player_inventory)


klim = create_new_player('Klim')
artem = create_new_player('Artem')
mark = create_new_player('Mark')
