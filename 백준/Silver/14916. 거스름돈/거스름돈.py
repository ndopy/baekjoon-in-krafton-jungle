import sys

change = int(sys.stdin.readline())
coins = [5, 2]
count = 0

if change == 1 or change == 3:
    print(-1)
else:
    count = change // 5
    remaining = change % 5

    if remaining % 2 == 0:
        count += remaining // 2
    else:
        count -= 1
        remaining += 5
        count += remaining // 2

    print(count)
