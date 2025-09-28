import math
import sys

# 난이도 의견의 개수
N = int(sys.stdin.readline().rstrip())

def solution(n):
    if n == 0:
        return 0

    levels = []

    # 난이도 저장
    for _ in range(n):
        level = int(sys.stdin.readline().rstrip())
        levels.append(level)

    # 난이도를 오름차순으로 정렬
    levels.sort()

    # 제외할 15% 인원 수 계산 : 반올림 (0.5 더하고 소수점 아래 버리기)
    count_to_exclude = int(n * 0.15 + 0.5)

    if count_to_exclude == 0:
        sliced_levels = levels
    else:
        # 배열 자르기 : 앞, 뒤에서 각각 count_to_exclude만큼 빼기
        sliced_levels = levels[count_to_exclude:-count_to_exclude]

    # 제외하고 남은 인원이 없으면 0 리턴하기
    if len(sliced_levels) == 0:
        return 0

    # 평균 구하기
    return int((sum(sliced_levels) / len(sliced_levels)) + 0.5)

print(solution(N))