import sys

while True:
    input_line = sys.stdin.readline()
    if not input_line:
        break

    answer = 0

    coupons, stamp_count_for_chicken = map(int, input_line.split())

    # 가지고 있는 쿠폰 개수만큼 더하기
    answer += coupons

    stamps = coupons

    # 서비스로 받을 수 있는 치킨 수 구하기
    while stamps // stamp_count_for_chicken > 0:
        service_chickens = stamps // stamp_count_for_chicken
        answer += service_chickens
        stamps = service_chickens + (stamps % stamp_count_for_chicken)

    print(answer)