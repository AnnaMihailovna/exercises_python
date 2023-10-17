from typing import List, Tuple


def read_input() -> Tuple[int, int, List[List[int]]]:
    n = int(input())
    m = int(input())
    matrix = ''
    matrix = [input().split(' ') for j in range(n)]
    return n, m, matrix

def transposition():
    n, m, matrix = read_input()
    for i in range(m):
        for j in range(n):
            print(matrix[j][i], end=' ')
        print('')

if __name__ == '__main__':
    transposition()
