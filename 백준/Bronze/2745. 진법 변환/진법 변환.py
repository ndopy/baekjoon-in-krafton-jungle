import sys

N, B = sys.stdin.readline().split()
B = int(B)
result = 0
multiplier = 1

for char in reversed(N):
    value = 0
    if '0' <= char <= '9':
        value = int(char)
    else:
        value = ord(char) - ord('A') + 10

    result += value * multiplier
    multiplier *= B

print(result)