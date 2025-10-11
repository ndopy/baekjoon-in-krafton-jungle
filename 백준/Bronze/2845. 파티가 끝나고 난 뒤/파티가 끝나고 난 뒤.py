import sys

L, P = map(int, sys.stdin.readline().split())

persons = L * P

papers = list(map(int, sys.stdin.readline().split()))

for i in papers:
    print(i - persons, end=' ')