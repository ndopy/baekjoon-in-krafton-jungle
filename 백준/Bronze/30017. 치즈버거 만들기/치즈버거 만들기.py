import sys

patty_count, cheese_count = map(int, sys.stdin.readline().split())

def solution(patty, cheese):
    burger_count = 0

    for i in range(1, cheese + 1):
        # 패티는 치즈보다 항상 1개 많아야 한다.
        if i + 1 <= patty:
            burger_count = i + (i + 1)
        else:
            break

    return burger_count

print(solution(patty_count, cheese_count))