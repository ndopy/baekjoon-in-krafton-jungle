import sys

ISBN_full = sys.stdin.readline().strip()

check_digit = ISBN_full[-1]
ISBN = ISBN_full[:-1]

asterisk_weight = 0
total_sum = 0

for idx, char in enumerate(ISBN):
    if char != '*':
        # 가중치를 (1, 3, 1, 3...) 곱한다
        # -> 짝수 번째 숫자만 곱해주면 된다.
        # -> 인덱스가 0부터 시작하므로 홀수 번째 인덱스만 3을 곱한다.
        if idx % 2 != 0:
            total_sum += int(char) * 3
        else:
            total_sum += int(char) * 1
    else:
        # '*'의 가중치 확인
        if idx % 2 != 0:
            asterisk_weight = 3
        else:
            asterisk_weight = 1

# check         = 10 - (sum + asterisk) % 10
# (sum + asterisk) % 10 = 10 - check

for asterisk_num in range(10):
    # check_digit이 0이면
    # -> 왼쪽 계산 결과는 항상 0 ~ 9인데, 오른쪽 계산 결과는 10이 되므로 절대로 같아질 수 없다.
    # -> 10 - int(check_digit) 을 10으로 나눈 나머지로 사용한다.
    is_valid = ((total_sum + (asterisk_num * asterisk_weight)) % 10) == (10 - int(check_digit)) % 10

    if is_valid:
        print(asterisk_num)
        break