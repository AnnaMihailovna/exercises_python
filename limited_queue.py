class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def push(self, item):
        if self.size < self.max_size:
            self.queue[self.tail] = item
            self.size += 1
            self.tail = (self.tail + 1) % self.max_size
        else:
            return 'error'
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]
    
    def pop(self):
        if self.is_empty():
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item
    
def main():
    number_commands = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    result = []
    for command in range(number_commands):
        command = input().split()
        if command[0] == 'push':
            a = queue.push(command[1])
            if a == 'error':
                result.append(a)
        elif command[0] == 'pop':
            result.append(queue.pop())
        elif command[0] == 'peek':
            result.append(queue.peek())
        elif command[0] == 'size':
            result.append(queue.size)
    for i in result:
        print(i)

if __name__ == '__main__':
    main()
