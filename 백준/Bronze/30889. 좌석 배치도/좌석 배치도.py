import sys
from pprint import pprint

N = int(sys.stdin.readline())

rows = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
}

# 좌석 배치도 : 10x20
seats = [['.' for _ in range(20)] for _ in range(10)]

# F16 -> F, 16 으로 분리하기
for _ in range(N):
    seat = sys.stdin.readline().strip()
    row = rows[seat[0]]
    col = int(seat[1:]) - 1
    seats[row][col] = 'o'

for row in seats:
    print(''.join(row))