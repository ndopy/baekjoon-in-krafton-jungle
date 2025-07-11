import sys

inputs = list(map(str, sys.stdin.read().split()))

a, b = inputs
b_nums = list(map(int, b))

for i in range(len(b_nums)):
    x = int(a)
    y = b_nums[len(b_nums) - i - 1]
    print(x * y)

print(int(a) * int(b))