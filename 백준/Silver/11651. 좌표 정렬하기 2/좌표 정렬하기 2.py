import sys

N = int(sys.stdin.readline())

coords = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coords.append((x, y))

coords.sort(key=lambda x: (x[1], x[0]))

for coord in coords:
    print(f"{coord[0]} {coord[1]}")