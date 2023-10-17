class Contestant:
    """Класс для представления участника соревнования."""
    def __init__(self, login, points, fine):
        self.login = login
        self.points = points
        self.fine = fine

    def __lt__(self, other):
        if not isinstance(other, Contestant):
            raise TypeError(
                f"Невозможно выполнить операцию сравнения между "
                f"{self.__class__.__name__} и {other.__class__.__name__}")
        return ((-self.points, self.fine, self.login) < 
                (-other.points, other.fine, other.login))

    def __str__(self):
        return self.login


def partition(contest_list, left, right):
    """Условно делит массив на две части относительно опорного элемента.
    Слева – элементы меньше. Справа – больше.
    Возвращает индекс элемента правого конца левой части.
    """
    pivot = (contest_list[left])
    i = left + 1
    j = right - 1
    while True:
        if (i <= j and contest_list[j] > pivot):
            j -= 1
        elif (i <= j and contest_list[i] < pivot):
            i += 1
        elif (contest_list[j] > pivot) or (contest_list[i] < pivot):
            continue
        if i <= j:
            contest_list[i], contest_list[j] = contest_list[j], contest_list[i]
        else:
            contest_list[left], contest_list[j] = contest_list[j], contest_list[left]
            return j

def quick_sort(contest_list, left, right):
    """Быстрая сортировка in-place."""
    if ((right - left) > 1):
        p = partition(contest_list, left, right)
        quick_sort(contest_list, left, p)
        quick_sort(contest_list, p + 1, right)
        return

def read_input():
    """Считывает входные данные из стандартного ввода.
     Преобразует их в список участников и возвращает его."""
    numbers = int(input())
    contest_list = []
    for _ in range(numbers):
        input_data = input().split()
        player = Contestant(input_data[0],
                            int(input_data[1]),
                            int(input_data[2]))
        contest_list.append(player)
    return contest_list

def main():
    """Основная логика программы."""
    contest_list = read_input()
    left = 0
    quick_sort(contest_list, left, len(contest_list))
    [print(i) for i in contest_list]

if __name__ == '__main__':
    main()
