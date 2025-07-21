import sys
from typing import Any

class Stack:
    class Empty(Exception):
        """비어 있는 FixedSizeStack 에 pop 또는 peek 할 때 내보내는 예외 처리"""
        pass

    class Full(Exception):
        """가득 차 있는 FixedSizeStack 에 push 할 때 내보내는 예외 처리"""
        pass

    def __init__(self, capacity: int = 10000) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0


    def push(self, value: Any) -> None:
        if self.is_full():
            raise Stack.Full

        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.is_empty():
            print(-1)
            return

        self.ptr -= 1
        print(self.stk[self.ptr])

    def empty(self) -> Any:
        if self.is_empty():
            print(1)
        else:
            print(0)

    def is_empty(self) -> Any:
        if self.ptr == 0:
            return 1
        else:
            return 0

    def is_full(self) -> bool:
        return self.ptr == self.capacity

    def size(self) -> Any:
        print(self.ptr)

    def top(self):
        if self.is_empty():
            print(-1)
            return

        print(self.stk[self.ptr - 1])

stack = Stack()

count = int(input())

for cnt in range(count):
    commands = sys.stdin.readline().split()
    command = commands[0]

    if command == 'push':
        stack.push(int(commands[1]))
    elif command == 'pop':
        stack.pop()
    elif command == 'top':
        stack.top()
    elif command == 'size':
        stack.size()
    elif command == 'empty':
        stack.empty()
