import random
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Player:
    """Класс для представления участника соревнования."""
    name: str
    solved: int
    penalty: int

    def __lt__(self, other):
        if not isinstance(other, Player):
            raise TypeError(
                f"Невозможно выполнить операцию сравнения между "
                f"{self.__class__.__name__} и {other.__class__.__name__}")
        return (-self.solved, self.penalty, self.name) < \
               (-other.solved, other.penalty, other.name)

    def __str__(self):
        return self.name


def partition(array: List[Player], pivot: Player, left: int, right: int) \
        -> Tuple[int, int]:
    """Условно делит массив на две части относительно опорного элемента.
    Слева – элементы меньше. Справа – больше.
    Возвращает индексы конца левой и начала правой части.
    """
    while left <= right:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return left, right


def quicksort(array: List[Player], start: int = 0, end: int = None):
    """Быстрая сортировка in-place. Опорный элемент рандомный."""
    if end is None:
        end = len(array) - 1
    if start >= end:
        return

    pivot = array[random.randint(start, end)]

    left, right = partition(array, pivot, start, end)
    quicksort(array, start, right)
    quicksort(array, left, end)


def read_input() -> List[Player]:
    """Считывает входные данные из стандартного ввода.
     Преобразует их в список участников и возвращает его."""
    lines = int(input())
    players = []
    for line in range(lines):
        input_data = input().split()
        player = Player(input_data[0],
                        int(input_data[1]),
                        int(input_data[2]))
        players.append(player)
    return players


def main() -> None:
    """Основная логика программы."""
    players = read_input()
    quicksort(players)
    [print(player) for player in players]



if __name__ == '__main__':
    main()