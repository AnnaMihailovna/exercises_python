# 88159154
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class Contestant:
    """Класс для представления участника соревнования."""
    login: str
    points: int
    fine: int

    def __lt__(self, other):
        if not isinstance(other, Contestant):
            raise TypeError(
                f"Невозможно выполнить операцию сравнения между "
                f"{self.__class__.__name__} и {other.__class__.__name__}")
        return ((-self.points, self.fine, self.login) < 
                (-other.points, other.fine, other.login))

    def __str__(self):
        return self.login


def partition(contest_list: List[Contestant], left: int, right: int) -> Tuple[int, int]:
    """Условно делит массив на две части относительно опорного элемента.
    Слева – элементы меньше. Справа – больше.
    Возвращает индексы конца левой и начала правой части.
    """
    pivot = contest_list[left]
    start = left
    end = right
    while start <= end:
        while contest_list[start] < pivot:
            start += 1
        while pivot < contest_list[end]:
            end -= 1
        if start <= end:
            contest_list[start], contest_list[end] = contest_list[end], contest_list[start]
            start += 1
            end -= 1
    return start, end

def quick_sort(contest_list: List[Contestant], left: int, right: int):
    """Быстрая сортировка in-place."""
    if (right - left) >= 1:
        start, end = partition(contest_list, left, right)
        quick_sort(contest_list, left, end)
        quick_sort(contest_list, start, right)

def read_input() -> List[Contestant]:
    """Считывает входные данные из стандартного ввода.
     Преобразует их в список участников и возвращает его."""
    numbers = int(input())
    contest_list = []
    for _ in range(numbers):
        login, points, fine = input().split()
        contest_list.append(
            Contestant(points=int(points), fine=int(fine), login=login))
    return contest_list

def main() -> None:
    """Основная логика программы."""
    contest_list = read_input()
    left = 0
    quick_sort(contest_list, left, len(contest_list)-1)
    [print(i) for i in contest_list]

if __name__ == '__main__':
    main()
