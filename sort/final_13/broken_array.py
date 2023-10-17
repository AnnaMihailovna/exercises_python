# 88142027
from typing import List

def broken_search(array: List[int], search_element: int) -> int:
    """Поиск в смещенном сортированном массиве.
    Возвращает индекс элемента.
    Если элемента нет в массиве, возвращает -1."""
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if search_element == array[mid]:
            return mid

        if array[left] <= array[mid]:
            if array[left] <= search_element <= array[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if array[mid] <= search_element <= array[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
