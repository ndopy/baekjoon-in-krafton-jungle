import sys

N = int(sys.stdin.readline())

numbers = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    numbers.append((x, y))

numbers.sort(key=lambda x: (x[0], x[1]))

for item in numbers:
    print(f"{item[0]} {item[1]}")