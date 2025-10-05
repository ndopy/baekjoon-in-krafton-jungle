import sys

odds = []

for _ in range(7):
    number = int(sys.stdin.readline())

    if number % 2:
        odds.append(number)

if odds:
    print(sum(odds))
    print(min(odds))
else:
    print(-1)
