import sys

n1, n2, n3 = list(map(int, sys.stdin.readline().split()))

def power(A, B, C):
    """A^B % C 를 구하는 함수"""

    if B == 0:
        return 1

    if B % 2 == 1:
        return ((A%C) * power(A, B-1, C)) % C
    else:
        half_power = power(A, B // 2, C)
        return (half_power * half_power) % C

print(power(n1, n2, n3))