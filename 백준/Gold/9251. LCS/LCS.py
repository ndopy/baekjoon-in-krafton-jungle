import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

def longest_common_subsequence(s1, s2):
    # s1, s2 에 대한 2차원 행렬 생성
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # i, j 모두 1부터 시작하지만 문자열은 0번 인덱스부터 검색해야 하기 때문에
            # i-1, j-1 부터 검색한다.
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

result = longest_common_subsequence(str1, str2)
print(result)