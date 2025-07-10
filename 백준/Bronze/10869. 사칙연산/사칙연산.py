import sys
numbers = list(map(int, sys.stdin.readline().split()))
a = int(numbers[0])
b = int(numbers[1])

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)