import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

class Stack:
    """Стек для хранения чисел."""
    def __init__(self):
        self._items = []

    def push(self, item):
        """Добавляет новый элемент в стек."""
        self._items.append(item)

    def pop(self):
        """Удаляет и возвращает последний элемент стека."""
        return self._items.pop()


def main():
    """Основная логика программы."""
    line = input().strip().split()
    stack = Stack()
    for element in line:
        if element in OPERATORS:
            b, a = stack.pop(), stack.pop()
            result = int(OPERATORS[element](a, b))
            stack.push(result)
        else:
            stack.push(int(element))
    return stack.pop()

if __name__ == '__main__':
    print(main())
