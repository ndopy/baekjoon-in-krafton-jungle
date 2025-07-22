import sys

paper_size = int(sys.stdin.readline())

colored_paper = []

for _ in range(paper_size):
    data = list(map(int, sys.stdin.readline().split()))
    colored_paper.append(data)

def is_mixed_color(paper, size, row, col):
    color = paper[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if paper[i][j] != color:
                return True
    return False

# 영역 내 모든 색종이들이 같은 색으로 칠해져 있는지
def check_paper(paper, size, row, col):

    if is_mixed_color(paper, size, row, col):
        # 다른 색깔이면 분할해서 다시 실행
        # 영역을 나눌 때마다 I, II, III, IV 4개 영역으로 나뉜다.
        blue1, white1 = check_paper(paper, size // 2, row, col)
        blue2, white2 = check_paper(paper, size // 2, row, col + size // 2)
        blue3, white3 = check_paper(paper, size // 2, row + size // 2, col)
        blue4, white4 = check_paper(paper, size // 2, row + size // 2, col + size // 2)

        return (blue1 + blue2 + blue3 + blue4,
                white1 + white2 + white3 + white4)
    else:
        # 같은 색깔일 때
        if paper[row][col] == 1:
            return 1, 0
        else:
            return 0, 1

blue, white = check_paper(colored_paper, paper_size, 0, 0)
print(white)
print(blue)