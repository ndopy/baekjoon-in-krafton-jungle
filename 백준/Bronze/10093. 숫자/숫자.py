import sys

a, b = map(int, sys.stdin.readline().split())

def solution(A, B):
    result = []
    
    if A == B:
        print(0)
        return

    # A, B를 정렬해야 한다.
    if A > B:
        A, B = B, A

    for i in range(A + 1, B):
        result.append(i)

    print(len(result))
    print(*result, sep=' ')

solution(a, b)