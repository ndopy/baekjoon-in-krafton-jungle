import sys

test_case_count = int(sys.stdin.readline().strip())

for _ in range(test_case_count):
    types_of_coins = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().strip().split()))
    target_value = int(sys.stdin.readline().strip())

    # dp 배열 생성
    # dp[i] : i원을 만들 수 있는 방법의 개수
    dp = [0] * (target_value + 1)
    # dp[0] : 0원을 만들 수 있는 방법은 모든 동전을 안 쓰는 방법밖에 없으므로 1이다.
    dp[0] = 1

    # 동전을 오름차순으로 정렬
    coins.sort()

    for coin in coins:
        for i in range(coin, target_value + 1):
            # dp[i] : 현재까지 구한 i원을 만드는 방법의 개수
            # dp[i - coin] : 현재 동전을 추가해서 i원을 만들 수 있는 방법의 개수
            dp[i] += dp[i - coin]

    print(dp[target_value])