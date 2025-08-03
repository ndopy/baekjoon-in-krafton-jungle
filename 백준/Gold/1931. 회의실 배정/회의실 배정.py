import sys

meeting_count = int(sys.stdin.readline())
meetings = []

# 회의 목록 만들기
for _ in range(meeting_count):
    start_time, end_time = map(int, sys.stdin.readline().split())
    meetings.append((start_time, end_time))

# 회의를 종료 시간 -> 시작 시간 순으로 정렬하기
meetings.sort(key=lambda x: (x[1], x[0]))

answer_count = 0
last_meeting_end_time = 0

for start_time, end_time in meetings:
    if start_time >= last_meeting_end_time:
        answer_count += 1
        last_meeting_end_time = end_time

print(answer_count)