import sys
N = int(sys.stdin.readline())

numbers = []

for number in range(N, 0, -1):
    numbers.append(str(number))

print("\n".join(numbers))