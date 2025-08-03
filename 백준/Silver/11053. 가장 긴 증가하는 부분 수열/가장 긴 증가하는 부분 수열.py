import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = [0] * len(numbers)
dp[0] = 1

for i in range(1, N):  # 현재 인덱스의 숫자와
    candidates = []

    for j in range(i): # 현재 인덱스보다 이전 숫자들을 비교하기
        current = numbers[i]
        prev = numbers[j]

        if prev < current:
            candidates.append(dp[j] + 1)

    if len(candidates) == 0:
        dp[i] = 1
    else:
        dp[i] = max(candidates)


print(max(dp))

