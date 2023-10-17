# 87294100
from typing import List, Tuple

def read_input() -> Tuple[int, List[List[str]]]:
    number_of_keys = int(input()) * 2
    char_field = [list(map(str, input())) for _ in range(4)]
    return number_of_keys, char_field

def number_of_points(number_of_keys: int,
                     char_field: List[List[str]]) -> int:
    points = 0
    keys = {str(i): 0 for i in range(0, 10)}
    for row in char_field:
        for key in row:
            if key.isdigit():
                keys[key] += 1
    for moment_of_time in range(0, 10):
            moment_of_time = str(moment_of_time)
            if keys[moment_of_time] and keys[moment_of_time] <= number_of_keys:
                points += 1
    return points

def main() -> None:
    number_of_keys, char_field = read_input()
    print(number_of_points(number_of_keys, char_field))

if __name__ == '__main__':
    main()
