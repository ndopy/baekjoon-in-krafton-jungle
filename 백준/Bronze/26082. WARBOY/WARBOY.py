import sys

A, B, C = map(int, sys.stdin.readline().split())

# 가성비
rival_pp = B // A

# WARBOY 의 성능 = (경쟁사 가성비 * 3) * 가격
print(3 * rival_pp * C)

