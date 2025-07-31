import sys

N = int(sys.stdin.readline())

def solve_01_tile(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)

    # 초기값 설정
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    return dp[n]

print(solve_01_tile(N))