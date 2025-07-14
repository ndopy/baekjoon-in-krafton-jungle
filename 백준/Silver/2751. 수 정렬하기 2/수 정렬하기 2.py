import sys

N = int(input())
numbers = list(map(int, sys.stdin.read().split()))

numbers.sort()

for number in numbers:
    print(number)