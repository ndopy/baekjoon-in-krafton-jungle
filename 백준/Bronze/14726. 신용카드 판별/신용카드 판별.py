import sys

T = int(sys.stdin.readline())

def luhn(num_str):
    # 숫자를 맨 우측부터 세어야하므로, 역순으로 정렬하기
    reversed_num_str = num_str[::-1]

    total_sum = 0

    for idx, num_char in enumerate(reversed_num_str):
        # 인덱스는 0부터 시작하므로, 홀수번째 인덱스 숫자를 2배, 짝수번째 인덱스 숫자는 그대로 두어야 한다.
        num = int(num_char)

        if idx % 2 == 1:
            doubled_num = num * 2

            # 10 이상인 경우, 각 자리의 숫자를 더하고 그 수로 대체한다.
            if doubled_num >= 10:
                doubled_num = (doubled_num // 10) + (doubled_num % 10)

            total_sum += doubled_num
        else:
            total_sum += num

    # 합이 10으로 나뉘면 T, 그렇지 않다면 F
    print('T') if total_sum % 10 == 0 else print('F')

for _ in range(T):
    card_number = sys.stdin.readline().strip()
    luhn(card_number)