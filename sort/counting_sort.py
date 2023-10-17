from typing import List


def counting_sort(array: List[int], k: int) -> None:
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for amount in range(1, counted_values[value]+1):
            array[index] = value
            print(array[index], end=' ')
            index += 1

counting_sort([0, 2, 1, 2, 0, 0, 1], 7)
