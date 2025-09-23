import sys

N = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())

dict = {}

for number in numbers:
    if number in dict:
        dict[number] += 1
    else:
        dict[number] = 1

M = int(sys.stdin.readline())
queries = map(int, sys.stdin.readline().split())
result = []

for query in queries:
    if query in dict:
        result.append(dict[query])
    else:
        result.append(0)

print(*result, sep=' ')