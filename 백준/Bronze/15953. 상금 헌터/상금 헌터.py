import sys

T = int(sys.stdin.readline())

prizes_in_2017 = [0] + ([500] * 1) + ([300] * 2) + ([200] * 3) + ([50] * 4) + ([30] * 5) + ([10] * 6) + ([0] * 79)
prizes_in_2018 = [0] + ([512] * 1) + ([256] * 2) + ([128] * 4) + ([64] * 8) + ([32] * 16) + ([0] * 33)

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    prize2017 = prizes_in_2017[a] * 10000
    prize2018 = prizes_in_2018[b] * 10000

    print(prize2017 + prize2018)
