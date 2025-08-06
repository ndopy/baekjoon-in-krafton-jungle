import sys

sum = 0

numbers = map(int, sys.stdin.readline().split())

for num in numbers:
    sum += num ** 2

print(sum % 10)