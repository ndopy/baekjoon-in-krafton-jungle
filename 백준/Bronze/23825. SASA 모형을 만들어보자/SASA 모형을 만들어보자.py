import sys

N, M = map(int, sys.stdin.readline().split())

# SASA 를 만드려면 S와 A가 각각 2개씩 필요하므로
# S, A를 2로 나눈 몫들 중에서 최소값이 바로 SASA를 만들 수 있는 개수의 최댓값이다.
S = N // 2
A = M // 2

print(min(S, A))