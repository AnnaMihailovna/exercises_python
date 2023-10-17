from typing import List


def colors_sort(colors: List[int], k: int=3) -> None:
    counted_values = [0] * k
    for value in colors:
        counted_values[value] += 1

    index = 0
    for value in range(k):
        for _ in range(0, counted_values[value]):
            colors[index] = str(value)
            index += 1
    print(' '.join(colors))

def main():
    _ = int(input())
    colors = [int(i) for i in input().split()]
    colors_sort(colors)

if __name__ == '__main__':
    main()
