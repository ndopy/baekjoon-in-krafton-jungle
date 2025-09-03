import sys

N, M = map(int, sys.stdin.readline().split())

money = N * 100

if money >= M:
    print('Yes')
else:
    print('No')