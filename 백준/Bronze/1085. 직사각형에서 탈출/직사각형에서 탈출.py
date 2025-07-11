import sys
inputs = list(map(int, sys.stdin.read().split()))
x, y, w, h = inputs

print(min(x, y, w-x, h-y))