from typing import List

def compare(obj_1: str, obj_2: str) -> bool:
    if int(obj_1 + obj_2) < int(obj_2 + obj_1):
        return True
    return False

def get_big_number(array: List[str], less: bool) -> str:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and less(array[j - 1], item_to_insert):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
    return ''.join(array)

def main() -> None:
    _ = int(input())
    array = [i for i in input().strip().split()]
    print(get_big_number(array, compare))


if __name__ == '__main__':
    main()
