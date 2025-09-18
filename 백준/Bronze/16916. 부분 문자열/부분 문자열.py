import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()

def get_pi(p):
    pi = [0] * len(p)
    j = 0               # 접두사와 접미사가 일치하는 길이

    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]

        # p[i] 와 p[j]가 같다면 = 일치하는 길이가 1 늘어난다.
        if p[i] == p[j]:
            j += 1
            pi[i] = j

    return pi

def kmp(s, p):
    n = len(s)
    m = len(p)
    pi = get_pi(p)
    j = 0   # 현재까지 일치한 패턴의 길이 (패턴의 인덱스)

    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = pi[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                return 1
            else:
                j += 1
    return 0

print(kmp(S, P))
