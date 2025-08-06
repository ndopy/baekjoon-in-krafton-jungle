import sys

test_case_count = int(sys.stdin.readline())

for _ in range(test_case_count):
    # 층, 각 층의 방의 수, 몇 번째 손님인지
    H, W, N = map(int, sys.stdin.readline().split())

    floor = (N - 1) % H + 1
    room_num = (N - 1) // H + 1

    print(floor * 100 + room_num)