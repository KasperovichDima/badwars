"""Magic methods hometask."""
from __future__ import annotations

from random import choice

names = 'Bob Charley Mike Don Viktor Jack Kurt Sam'.split()
last_names = 'Smith Johson Cooper Karlos Santiago Stanley'.split()


def get_random_player() -> FootballPlayer:
    """Get new player with random name and last name."""
    return FootballPlayer(choice(names), choice(last_names))  # noqa: S311


class FootballPlayer:
    """Football player with name and last name."""

    def __init__(self, name: str, last_name: str) -> None:
        """Initializtion."""
        self.name = name
        self.last_name = last_name

    def __repr__(self) -> str:
        return f'[{self.name} {self.last_name}]'

class FootballTeam:
    """Team of 11 football players."""

    def __init__(self) -> None:
        """Create team."""
        self.players = [get_random_player() for _ in range(11)]
        self.__index = 0

    def add_player(self, player: FootballPlayer) -> None:
        """Add new player to team."""
        self.players.append(player)

    def remove_player(self, player_number: int) -> None:
        """Remove player specified by number from team."""
        self.players.pop(player_number - 1)

    def __repr__(self) -> str:
        """Напечатать команду.

        * Созадем пустую строку к которой затем будем добавлять игроков.
        * В цикле for перебираем всех игроков из списка self.players
          предварительно применив к нему enumerate.
        * Добавляем номер и игрока к результату + перенос на новую строку.
        * Возвращаем получившийся результат.
        """
        result = ''
        for num, player in enumerate(self.players, 1):
            result += f'{num}: {player}\n'
        return result

    def __bool__(self) -> bool:
        """Return True if team is complete (11 or more players)."""
        return len(self.players) >= 11

    def __len__(self) -> int:
        """Get team size."""
        return len(self.players)

    def __iter__(self):
        return iter(self.players)

    def __next__(self) -> FootballPlayer:
        try:
            next_player = self.players[self.__index]
        except IndexError:
            raise StopIteration
        self.__index += 1
        return next_player

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

# Реализовать метод __iter__ чтобы команду можно было перебрать в цикле for.

# Реализовать метод __next__ чтобы команду можно было получить следующего игрока.


team = FootballTeam()
# team.remove_player(7)

# for player in team:
#     print(f'Делаю селфи с моим кумиром: {player}')

