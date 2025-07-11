import sys
numbers = list(map(int, sys.stdin.read().split()))

max_num = max(numbers)
print(max_num)
print(numbers.index(max_num) + 1)