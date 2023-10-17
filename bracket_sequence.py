PATTERN = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Bracket:
    def __init__(self):
        self.brackets = []

    def is_empty(self):
        return self.brackets == []

    def push(self, item):
        self.brackets.append(item)

    def pop(self):
        return self.brackets.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.brackets[-1]


def main():
    brackets_input = input()
    seq = Bracket()
    for bracket in brackets_input:
        if bracket in PATTERN.keys():
            seq.push(bracket)
        elif not seq.is_empty() and PATTERN.get(seq.peek()) == bracket:
            seq.pop()
        else:
            seq.push(bracket)
            break
    print(seq.is_empty())


if __name__ == '__main__':
    main()
