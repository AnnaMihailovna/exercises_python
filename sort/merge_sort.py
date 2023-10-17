from typing import List


def merge(arr: List[int], lf: int, mid: int, rg: int) -> List[int]:
    left_array = arr[lf: mid]
    right_array = arr[mid: rg]

    l, r, k = 0, 0, lf
    while l < len(left_array) and r < len(right_array):
        if left_array[l] <= right_array[r]:
            arr[k] = left_array[l]
            l += 1
        else:
            arr[k] = right_array[r]
            r += 1
        k += 1

    while l < len(left_array):
        arr[k] = left_array[l]
        l += 1
        k += 1
    while r < len(right_array):
        arr[k] = right_array[r]
        r += 1
        k += 1
    return arr


def merge_sort(arr: List[int], lf: int, rg: int) -> None:
    if rg - lf <= 1:
        return
    else:
        mid = (lf + rg) // 2
        merge_sort(arr, lf, mid)
        merge_sort(arr, mid, rg)
        merge(arr, lf, mid, rg)


def test() -> None:
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected
    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0 , 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected

if __name__ == '__main__':
    test()
