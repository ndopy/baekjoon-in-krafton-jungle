import sys

row, col = map(int, sys.stdin.readline().split())
board = []

for i in range(row):
    board.append(list(sys.stdin.readline().strip()))

# 각 행을 순회하면서 가로 판자('-') 개수 세기
def count_horizontal():
    count = 0
    for current_row in range(row):  # 각 행을 순회
        current_col = 0

        while current_col < col:  # 현재 행의 각 열을 순회
            if board[current_row][current_col] == '-':  # 가로 판자('-')를 발견하면
                while current_col < col and board[current_row][current_col] == '-':  # 연속된 가로 판자를 하나로 세기
                    current_col += 1
                count += 1  # 하나의 가로 판자로 세기

            current_col += 1
    return count


# 각 열을 순회하면서 세로 판자('|') 개수를 세기
def count_vertical():
    count = 0
    for current_col in range(col):
        current_row = 0

        while current_row < row:
            if board[current_row][current_col] == '|':  # 세로 판자('|')를 발견하면
                while current_row < row and board[current_row][current_col] == '|':  # 연속된 세로 판자를 하나로 세기
                    current_row += 1
                count += 1  # 하나의 세로 판자로 세기
            current_row += 1

    return count

result = count_horizontal() + count_vertical()
print(result)
