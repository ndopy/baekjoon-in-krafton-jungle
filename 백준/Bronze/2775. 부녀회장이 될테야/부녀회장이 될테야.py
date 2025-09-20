import sys

max_floor = 15
max_room = 15

memo = [[0] * max_room for _ in range(max_floor)]

# k층의 n호에 사는 사람 수 구하기
def get_people_recursive(k, n):
    # 종료 조건: 0층인 경우 n호실에 사는 사람 수는 n명이다.
    if k == 0:
        return n

    # 어떤 층이든 1호실에는 반드시 1명만 산다.
    if n == 1:
        return 1

    if memo[k][n] != 0:
        return memo[k][n]

    # k층의 n호에 사는 사람 수
    memo[k][n] = get_people_recursive(k-1, n) + get_people_recursive(k, n-1)
    return memo[k][n]

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(get_people_recursive(k, n))
