import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

best_sum = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            current_sum = cards[i] + cards[j] + cards[k]

            if current_sum <= M and current_sum > best_sum:
                best_sum = current_sum

print(best_sum)