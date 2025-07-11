import sys

# N 은 1,000보다 작거나 같은 자연수
N = int(sys.stdin.readline())

def is_hansu(num: int) -> bool:
    if num < 100:
        return True

    a = num // 100
    b = (num // 10) % 10
    c = num % 10

    return (b - a) == (c - b)

def get_count_of_hansu(n: int) -> int:
    # 1 ~ 99 : 모두 한수
    limit = min(n, 999)
    count = min(n, 99)

    for i in range(100, limit + 1):
        if is_hansu(i):
            count += 1
    return count

answer = get_count_of_hansu(N)
print(answer)