from typing import List, Tuple


def read_input() -> Tuple[int, int, List[int], List[int]]:
    n = int(input())
    m = int(input())
    north = [int(i) for i in input().split()]
    south = [int(i) for i in input().split()]
    return n, m, north, south


def get_median(left: List[int], right: List[int]):
    array = merge(left, right)
    mid = len(array) // 2
    if len(array) % 2:
        return array[mid]
    return (array[mid] + array[mid - 1]) / 2


def merge(left: List[int], right: List[int]):
    len_l = len(left)
    len_r = len(right)
    lt = rg = i = 0
    result = [0] * (len_l + len_r)

    while lt < len_l and rg < len_r:
        if left[lt] <= right[rg]:
            result[i] = left[lt]
            lt += 1
        else:
            result[i] = right[rg]
            rg += 1
        i += 1

    while lt < len_l:
        result[i] = left[lt]
        lt += 1
        i += 1
    while rg < len_r:
        result[i] = right[rg]
        rg += 1
        i += 1

    return result


def main() -> None:
    _, _, north, south = read_input()
    print(get_median(north, south))


if __name__ == '__main__':
    main()
