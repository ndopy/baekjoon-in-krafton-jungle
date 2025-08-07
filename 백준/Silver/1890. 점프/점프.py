import sys

board_size = int(sys.stdin.readline())
board = []

# 입력값에 맞게 보드 생성하기
for i in range(board_size):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

# dp 배열을 생성하여 board[i][j] 각 위치에 도달할 수 있는 경로의 수를 저장하기
dp = [[0] * board_size for _ in range(board_size)]

# dp[0][0]을 1로 초기화
dp[0][0] = 1

for i in range(board_size):
    for j in range(board_size):
        # 현재 위치의 점프 거리가 0보다 크고, 현재 위치에 도달할 수 있는 경로가 있다면
        if board[i][j] > 0 and dp[i][j] > 0:
            jump_range = board[i][j]

            if i + jump_range < board_size:  # 아래쪽으로 점프
                dp[i + jump_range][j] += dp[i][j]
            if j + jump_range < board_size:  # 오른쪽으로 점프
                dp[i][j + jump_range] += dp[i][j]

print(dp[board_size - 1][board_size - 1])
