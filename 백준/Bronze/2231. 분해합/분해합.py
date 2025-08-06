import sys

N = int(sys.stdin.readline())
len_N = int(len(str(N)))

result = []

for num in range(1, N):
    bbh_1 = num
    bbh_2 = 0

    for i in range(len_N - 1, -1, -1):
        bbh_2 += num // 10 ** i
        num = num % 10 ** i

    bbh = bbh_1 + bbh_2

    if bbh == N:
        result.append(bbh_1)
        break

if not result:
    print(0)
else:
    print(result[0])