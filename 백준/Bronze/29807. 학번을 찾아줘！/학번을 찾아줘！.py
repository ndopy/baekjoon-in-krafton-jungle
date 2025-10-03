import sys

T = int(sys.stdin.readline())

def solution(T):
    scores = [0, 0, 0, 0, 0]
    inputs = list(map(int, sys.stdin.readline().split()))

    for i in range(T):
        scores[i] = inputs[i]

    # 국어, 수학, 영어, 탐구, 제2외국어
    a, b, c, d, e = scores

    sum_of_score = 0

    # 국어 - 영어 비교
    if a > c:
        sum_of_score += (a - c) * 508
    else:
        sum_of_score += (c - a) * 108

    # 수학 - 탐구 비교
    if b > d:
        sum_of_score += (b - d) * 212
    else:
        sum_of_score += (d - b) * 305

    if e > 0:
        sum_of_score += e * 707

    return sum_of_score * 4763


print(solution(T))
