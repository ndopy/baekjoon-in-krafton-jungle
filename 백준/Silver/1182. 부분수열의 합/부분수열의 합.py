# 1182 - 부분수열의 합

# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이  S 가 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys

def solution(numbers, target_sum, index, current_sum, count):
    # 현재 인덱스가 배열의 길이와 같다면 종료
    if index == len(numbers):
        # 현재 합이 목표 합과 같고, 크기가 양수인 부분수열이라면
        if current_sum == target_sum and count > 0:
            global answer
            answer += 1
        return 0

    # 현재 숫자를 포함할 때
    include = solution(numbers, target_sum, index + 1, current_sum + numbers[index], count + 1)

    # 현재 숫자를 포함하지 않는 경우
    exclude = solution(numbers, target_sum, index + 1, current_sum, count)

    # 두 경우의 수를 합하여 반환
    return include + exclude

first_line = list(map(int, sys.stdin.readline().split()))
N = first_line[0]
S = first_line[1]
numbers = list(map(int, sys.stdin.readline().split()))
answer = 0


solution(numbers, S, 0, 0, 0)
print(answer)
