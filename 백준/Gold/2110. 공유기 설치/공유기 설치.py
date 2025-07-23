import sys

house_count, wifi_count = map(int, sys.stdin.readline().split())
houses = list(map(int, sys.stdin.read().split()))

# 오름차순 정렬하기
houses.sort()

left = 1
right = houses[-1] - houses[0]

max_interval_found = 0

def check_installation(interval):
    installed_count = 1
    last_installed_coord = houses[0]

    # 공유기를 첫 번째 집에 설치하고 시작하기
    for idx in range(1, len(houses)):
        current_house = houses[idx]
        if current_house >= last_installed_coord + interval:
            installed_count += 1
            last_installed_coord = current_house

    return installed_count >= wifi_count

while left <= right:
    current_minimum_interval = (left + right) // 2

    # 현재 최소 간격으로 공유기 wifi_count 만큼 설치할 수 있는가?
    is_possible = check_installation(current_minimum_interval)

    if not is_possible:
        # 최소 거리를 좁혀야 한다.
        right = current_minimum_interval - 1
    else:
        # 일단 설치가 가능한 상태지만, 더 긴 최소 거리가 있는지 찾아본다.
        max_interval_found = current_minimum_interval
        left = current_minimum_interval + 1

print(max_interval_found)