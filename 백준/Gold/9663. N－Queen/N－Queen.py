N = int(input())
answer_count = 0

# 퀸이 놓인 열(column) 위치를 기록할 리스트
column_with_queen = [0] * N

# 각 row 에 퀸이 존재하는지 기록할 리스트
exist_in_row = [False] * N

# 대각선 방향에 퀸이 존재하는지 기록할 리스트
exist_in_diag_sum = [False] * (2 * N - 1)       # row + col 값이 같음
exist_in_diag_diff = [False] * (2 * N - 1)       # row - col 값이 같음.)

def set_queen(column_idx):
    global answer_count

    # 탈출 조건 : 모든 열에 퀸을 다 놓았다면
    if column_idx == N:
        # 정답 개수 +1 증가
        answer_count += 1
        return

    # 현재 columnIdx 열의 각 rowIdx 에 퀸을 놓아보기
    for row_idx in range(N):        # 4x4 라면 rowIdx 범위: 0, 1, 2, 3
        if (not exist_in_row[row_idx]
            and not exist_in_diag_sum[row_idx + column_idx]
            and not exist_in_diag_diff[row_idx - column_idx + N - 1]):

            # 퀸을 (columnIdx, rowIdx) 에 놓았다고 위치 표시하기 ex. 0열의 0행에 놓았어.
            column_with_queen[column_idx] = row_idx

            # 퀸의 위치와 같은 행, 대각선에 사용중임을 표시하기
            exist_in_row[row_idx] = True                              # 현재 행
            exist_in_diag_sum[row_idx + column_idx] = True            # 대각선 1
            exist_in_diag_diff[row_idx - column_idx + N - 1] = True   # 대각선 2

            # 다음 열로 이동해서 퀸을 놓으라고 재귀 호출
            set_queen(column_idx + 1)

            # 백트래킹
            # 다음 퀸을 놓는 호출이 끝났으니, 현재 위치의 퀸을 치우고
            # 다른 row_idx 에도 놓아볼 수 있도록 상태를 되돌림.
            exist_in_row[row_idx] = False  # 현재 행
            exist_in_diag_sum[row_idx + column_idx] = False  # 대각선 1
            exist_in_diag_diff[row_idx - column_idx + N - 1] = False  # 대각선 2


# N-Queen 문제 시작: 0번째 열부터 퀸을 놓기 시작
set_queen(0)
print(f"{answer_count}")