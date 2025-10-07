import sys

N = int(sys.stdin.readline())

pictures = []

for order in range(N):
    picture = []
    for i in range(5):
        picture.append(list(sys.stdin.readline().strip()))

    pictures.append(picture)

min_diff = 100
answer_a = 0
answer_b = 0

# 그림 2개씩 비교하기
for i in range(0, N):
    for j in range(i + 1, N):

        current_diff = 0

        for row in range(5):
            for col in range(7):
                if pictures[i][row][col] != pictures[j][row][col]:
                    current_diff += 1

        if current_diff < min_diff:
            min_diff = current_diff
            answer_a = i
            answer_b = j

print(answer_a + 1, answer_b + 1)