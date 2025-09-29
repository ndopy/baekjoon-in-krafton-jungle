import sys
from collections import deque

N = int(sys.stdin.readline())

def solution(n):
    queue = deque()

    for _ in range(n):
        command = sys.stdin.readline()

        if command.startswith('push'):
            number = int(command.split()[1])
            queue.append(number)
        elif command.startswith('pop'):
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif command.startswith('size'):
            print(len(queue))
        elif command.startswith('empty'):
            print(0 if queue else 1)
        elif command.startswith('front'):
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif command.startswith('back'):
            if queue:
                print(queue[-1])
            else:
                print(-1)

solution(N)