import sys

N = int(sys.stdin.readline())

def solution(n):
    count_5kg = 0
    count_3kg = 0

    if n % 5 == 0:      # n이 5의 배수이면
        return n // 5

    # 설탕 봉지 : 5kg, 3kg
    # 1. 5kg 로 나누기
    count_5kg = n // 5
    n -= 5 * (n // 5)

    # 2. 남은 nkg를 3kg 로 나눠보기
    if n % 3 == 0: # 3kg로 나누어 떨어지면
        count_3kg = n // 3
        return count_5kg + count_3kg
    else:
        if count_5kg == 0:  # 5kg짜리도 없으면 -1 리턴
            return -1

        while count_5kg > 0:
            # 5kg를 다시 채우고, 3kg로 나누기
            count_5kg -= 1
            n += 5

            if n % 3 == 0:
                count_3kg += n // 3
                n -= (n // 3) * 3
                break

    # 정확히 nkg로 맞출 수 없으면 -1 리턴
    if n != 0:
        return -1

    return count_5kg + count_3kg

result = solution(N)
print(result)