import sys

ax, ay, az = map(int, sys.stdin.readline().split())
cx, cy, cz = map(int, sys.stdin.readline().split())

bx = cx - az
by = int(cy / ay)
bz = cz - ax

print(f"{bx} {by} {bz}")