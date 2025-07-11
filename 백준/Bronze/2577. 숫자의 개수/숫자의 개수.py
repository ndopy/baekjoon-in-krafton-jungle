import sys

A, B, C = list(map(int, sys.stdin.read().split()))

result = str(A * B * C)
numbers_ABC = list(map(int, list(result)))

counts = [0] * 10

for digit in result:
    counts[int(digit)] += 1

for count in counts:
    print(count)
