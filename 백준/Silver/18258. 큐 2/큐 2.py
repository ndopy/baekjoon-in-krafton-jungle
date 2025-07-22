import sys
from typing import Any

class FixedSizeQueue:
    class Full(Exception):
        pass

    class Empty(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.no = 0
        self.que = ["None"] * capacity
        self.front = 0
        self.rear = 0

    def is_full(self):
        return self.no ==  self.capacity

    def is_empty(self):
        return self.no == 0

    def size(self):
        print(self.no)

    def push(self, value: Any) -> None:
        if self.is_full():
            # raise FixedSizeQueue.Full
            return

        self.que[self.rear] = value
        self.rear += 1
        self.no += 1

        if self.rear == self.capacity:
            self.rear = 0

    def pop(self) -> Any:
        if self.is_empty():
            print(-1)
            return

        data = self.que[self.front]
        self.front += 1
        self.no -= 1

        if self.front == self.capacity:
            self.front = 0

        print(data)
        # return data

    def get_front(self):
        if self.is_empty():
            print(-1)
            return

        print(self.que[self.front])
        # return self.que[self.front]

    def get_back(self):
        if self.is_empty():
            print(-1)
            return

        print(self.que[self.rear - 1])
        # return self.que[self.rear - 1]

    def empty(self):
        print(1) if self.no == 0 else print(0)

queue = FixedSizeQueue(2_000_000)

commands_count = int(sys.stdin.readline())

command_map = {
    'push': queue.push,
    'pop': queue.pop,
    'size': queue.size,
    'empty': queue.empty,
    'front': queue.get_front,
    'back': queue.get_back
}

for _ in range(commands_count):
    commands = list(sys.stdin.readline().split())
    command_name = commands[0]

    if command_name in command_map:
        action = command_map[command_name]

        if command_name == 'push':
            queue.push(commands[1])
        else:
            action()