import sys

total_sum = 0

for _ in range(5):
    score = int(sys.stdin.readline())
    total_sum += score

print(total_sum)