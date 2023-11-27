"""Протокол отвечает на вопрос "Что делает?".

Класс отвечает на вопрос "Как делает?"

Объект класса это делает.
"""

from typing import Protocol


class SoundableNotAlive(Protocol):
    """Soundable protocol.

    Протокол отвечает на вопрос "Что делает?"
    """

    def make_sound(self) -> None: ...


class Cow:
    """Конкретный класс.

    Класс отвечает на вопрос "Как делает?"
    """

    def make_sound(self) -> None:
        print('Moooooo!')

    def eat(self, food): ...

    def sleep(self, time): ...


#  Объект класса это делает.
c = Cow()
c.make_sound()
