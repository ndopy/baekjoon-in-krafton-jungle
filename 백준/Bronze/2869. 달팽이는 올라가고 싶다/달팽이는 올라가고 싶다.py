import sys, math

day, night, goal = list(map(int, sys.stdin.readline().split()))

# 하루에 올라가는 높이
daily_climb = day - night

# 마지막 날 1일 추가
day_count = math.ceil((goal - day) / daily_climb) + 1
print(day_count)
