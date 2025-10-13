import sys

N = int(sys.stdin.readline())

for _ in range(N):
    num = int(sys.stdin.readline())

    if num % 2:
        print('odd')
    else:
        print('even')