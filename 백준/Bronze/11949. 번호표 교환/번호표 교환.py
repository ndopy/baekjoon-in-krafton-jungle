import sys

N, M = map(int, sys.stdin.readline().split())


# 학생들의 번호표 담기
students = []

for _ in range(N):
    students.append(int(sys.stdin.readline()))

# 1 ~ M까지의 카드로 게임 시작
for card in range(1, M + 1):
    for j in range(N - 1):
        if (students[j] % card) > (students[j + 1] % card):
            students[j], students[j + 1] = students[j + 1], students[j]

for student in students:
    print(student)