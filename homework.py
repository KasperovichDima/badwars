"""Magic methods hometask."""
from random import choice

names = 'Bob Charley Mike Don Viktor Jack Kurt Sam'
last_names = 'Smith Johson Cooper Karlos Santiago Stanley'


class FootballPlayer:
    """Football player with name and last name."""

    def __init__(self, name: str, last_name: str) -> None:
        """Initializtion."""
        self.name = name
        self.last_name = last_name


def get_random_player() -> FootballPlayer:
    """Get new player with random name and last name."""
    return FootballPlayer(choice(names), choice(last_names))  # noqa: S311

class FootballTeam:
    """Team of 11 football players."""

    def __init__(self) -> None:
        """Create team."""
        self.players = [get_random_player() for _ in range(11)]


# Задание:
# * Реализовать метод __repr__ у игрока, чтобы выводилась его имя и фамилия.

# * Реализовать метод __repr__ у команды, чтобы выводились все ее игроки
#   строка за строкой с номером по порядку.

# * Добавить у команды метод add_player, который принимает FootballPlayer
#   и добавляет его в список игроков команды.

# * Добавить у команды метод remove_player, который принимает число
#   (порядковый номер) и удаляет его из списка игроков команды.

# * Реализовать у команды метод __bool__, который возвращает True,
#   если в команде 11 и более игроков.

# * Реализовать у команды метод __len__,
#   который возвращает количество игроков в команде.




# Материалы:

# https://www.stratascratch.com/blog/7-magic-methods-that-will-turn-you-into-a-python-wizard/