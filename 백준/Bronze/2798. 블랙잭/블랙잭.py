import sys

N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

answers = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum_of_three_cards = cards[i] + cards[j] + cards[k]

            if sum_of_three_cards <= M:
                answers.append(sum_of_three_cards)

print(max(answers))