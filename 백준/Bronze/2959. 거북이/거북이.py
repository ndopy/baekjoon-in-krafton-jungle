import sys

numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

area = numbers[0] * numbers[2]
print(area)