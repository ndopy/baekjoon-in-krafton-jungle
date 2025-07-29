import sys
from collections import deque

# 1 ~ N-1 까지는 기본 부품 또는 중간 부품, N 은 완제품 번호
N = int(sys.stdin.readline())

# 부품들 관계도 개수
M = int(sys.stdin.readline())

# 각 부품이 다른 부품을 얼마나 필요로 하는지 저장하는 리스트
needs = [[] for _ in range(N + 1)]

# 각 부품의 진입 차수를 저장하는 리스트
indegree = [0] * (N + 1)

# 각 부품을 만드는데 필요한 기본 부품의 개수를 저장하는 2차원 리스트
parts = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    # Y가 K개 있어야 X가 된다. (y * k-> x)
    x, y, k = map(int, sys.stdin.readline().split())
    needs[y].append((x, k)) # y는 x를 만드는 데에 k개 필요하다. ???

    indegree[x] += 1

queue = deque()

# 진입 차수가 0인 부품(=기본 부품)을 큐에 추가
for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)
        parts[i][i] = 1     # 기본 부품은 자기 자신을 만드는 데에 1개가 필요하다.

while queue:
    current_part = queue.popleft()

    # 현재 부품으로 만들 수 있는 다른 부품들을 확인하기
    for next_part, count in needs[current_part]:

        # next_part 를 조립하는 데에 필요한 기본 부품의 개수를 갱신한다.
        for i in range(1, N + 1):
            # next_part 를 만드는 데 필요한 부품 i의 총 개수는
            # [현재 부품 1개를 만드는 데에 필요한 부품 i 의 개수] X [next_part 를 만들 때 필요한 current_part의 개수]
            parts[next_part][i] += parts[current_part][i] * count

        indegree[next_part] -= 1

        if indegree[next_part] == 0:
            queue.append(next_part)

# 완제품(N)을 만드는 데 필요한 기본 부품들 출력
for i in range(1, N + 1):
    if parts[N][i] > 0:
        print(i, parts[N][i])