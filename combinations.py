BUTTONS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def combinations(numbers: str, result: str ='') -> None:
    if not numbers:
        print(result, end=' ')
        return
    for letter in BUTTONS[numbers[0]]:
        result += letter
        combinations(numbers[1:], result)
        result = result[:-1]

if __name__ == '__main__':
    combinations(input())
