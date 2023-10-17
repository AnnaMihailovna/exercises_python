def find_perimeter(array):
    for index in range(0, len(array) - 2):
        if array[index] < (array[index + 1] + array[index + 2]):
            return array[index] + array[index + 1] + array[index + 2]


if __name__ == '__main__':
    _ = int(input())
    array = sorted([int(num) for num in input().split(' ')], reverse=True)
    print(find_perimeter(array))
