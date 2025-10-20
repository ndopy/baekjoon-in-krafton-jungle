# 해밍 거리 : 두 숫자의 서로 다른 자리수의 개수
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    hamming_distance = 0

    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            hamming_distance += 1

    print(f"Hamming distance is {hamming_distance}.")