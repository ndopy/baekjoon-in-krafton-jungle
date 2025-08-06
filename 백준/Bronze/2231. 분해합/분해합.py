import sys

N = int(sys.stdin.readline())

result = 0

for i in range(1, N + 1):
    sum_digits = sum(map(int, str(i)))

    if i + sum_digits == N:
        result = i
        break

print(result)