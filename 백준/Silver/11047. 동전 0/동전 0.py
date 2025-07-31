import sys

N, money = map(int, sys.stdin.readline().split())

coins = []

for _ in range(N):
    coin = int(sys.stdin.readline())
    coins.append(coin)

# 동전의 가치가 높은 순으로(=내림차순) 정렬하기
coins.sort(reverse=True)

coin_count = 0

for coin in coins:
    if money >= coin:
        coin_count += money // coin
        money %= coin

print(coin_count)