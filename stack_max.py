class StackMax:
    def __init__(self):
        self.numbers = []

    def push(self, number):
        self.numbers.append(number)

    def pop(self):
        if self.numbers:
            return self.numbers.pop()
        print('error')

    def get_max(self):
        print(max(self.numbers) if self.numbers else None)


def read_input():
    n = int(input())
    commands = [list(map(str, input().split())) for _ in range(n)]
    return commands


def main():
    commands = read_input()
    stack = StackMax()
    for command in commands:
        if command[0] == 'push':
            stack.push(int(command[1]))
        if command[0] == 'pop':
            stack.pop()
        if command[0] == 'get_max':
            stack.get_max()


if __name__ == '__main__':
    main()
