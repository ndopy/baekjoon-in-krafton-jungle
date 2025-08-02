import sys

N, K = map(int, sys.stdin.readline().strip().split())

def knapsack(max_weight):
    dp = [0] * (K + 1)

    for _ in range(N):
        item_weight, item_value = map(int, sys.stdin.readline().strip().split())

        for current_knapsack_weight in range(max_weight, item_weight - 1, -1):
            # 현재 물건을 안 넣는 경우
            item_not_included = dp[current_knapsack_weight]

            # 현재 물건을 넣는 경우
            # [현재 물건의 가치] + [배낭에서 현재 무게를 뺀 남은 무게의 가치]
            item_included = dp[current_knapsack_weight - item_weight] + item_value

            dp[current_knapsack_weight] = max(item_not_included, item_included)

    return dp[max_weight]

print(knapsack(K))