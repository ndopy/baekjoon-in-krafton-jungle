import sys

H, I, A, R, C = map(int, sys.stdin.readline().rstrip().split())

print((H * I) - (A * R * C))