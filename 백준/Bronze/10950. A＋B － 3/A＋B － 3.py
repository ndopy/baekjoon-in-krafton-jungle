n = int(input())
pairs = [tuple((map(int, input().split()))) for _ in range(n)]

for a, b in pairs:
    print(a + b)