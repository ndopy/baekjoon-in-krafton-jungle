import sys

def factorial(n):
    sum = 1

    for i in range(n, 0, -1):
        sum *= i

    return sum

N, K = map(int, sys.stdin.readline().split())

print(factorial(N) // (factorial(K) * factorial(N - K)))