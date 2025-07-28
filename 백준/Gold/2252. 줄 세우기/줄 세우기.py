import sys
from collections import deque

student_count, comparing_count = map(int, sys.stdin.readline().split())

# 학생 번호가 1부터 시작한다는 점에 유의할 것.
graph = {i: [] for i in range(student_count + 1)}
in_degree = [0] * (student_count + 1)

queue = deque()
result = []

for _ in range(comparing_count):
    student_a, student_b = map(int, sys.stdin.readline().split())

    # 그래프 업데이트 (방향 그래프임에 유의하기)
    graph[student_a].append(student_b)

    # in_degree 업데이트
    in_degree[student_b] += 1

for i in range(1, student_count + 1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    current_student = queue.popleft()
    result.append(current_student)

    # 현재 학생과 이웃한 학생들에 대해서 in_degree 를 감소시키고,
    # 그 결과로 만약 in_degree 가 0이 되면 큐에 추가한다.
    for neighbor in graph[current_student]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

print(' '.join(map(str, result)))