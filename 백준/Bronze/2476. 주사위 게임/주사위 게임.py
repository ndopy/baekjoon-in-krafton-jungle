import sys

N = int(sys.stdin.readline())

highest_prize = 0

for _ in range(N):
    a, b, c = list(map(int, sys.stdin.readline().split()))
    current_prize = 0

    if a == b == c:
        current_prize = 10_000 + (a * 1_000)
    elif (a == b and b != c) or (a == c and a != b) or (b == c and a != b):
        if a == b:
            current_prize = 1_000 + (a * 100)
        elif a == c:
            current_prize = 1_000 + (a * 100)
        else:
            current_prize = 1_000 + (b * 100)
    else:
        current_prize = max(a, b, c) * 100

    if current_prize > highest_prize:
        highest_prize = current_prize

print(highest_prize)