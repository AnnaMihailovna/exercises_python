from typing import List


def read_input():
    _ = int(input())
    factors = [int(i) for i in input().split()]
    _ = int(input())
    sizes = [int(i) for i in input().split()]
    return factors, sizes


def how_happy(factors: List[int], sizes: List[int]):
    factors.sort(reverse=True), sizes.sort(reverse=True)
    result = 0
    i = 0
    for factor in factors:
        if i < len(sizes) and factor <= sizes[i]:
            i += 1
            result += 1
    return result


def main():
    factors, sizes = read_input()
    print(how_happy(factors, sizes))


if __name__ == '__main__':
    main()

# with open("input.txt") as f:
#     n = int(f.readline())
#     factor = sorted(list(map(int, f.readline().split())), reverse=True)
#     m = int(f.readline())
#     sizes = sorted(list(map(int, f.readline().split())))

# happy_child = 0

# for i in range(len(factor)):
#     if sizes and factor[i] <= sizes[-1]:
#         sizes.pop()
#         happy_child += 1

# print(happy_child)
