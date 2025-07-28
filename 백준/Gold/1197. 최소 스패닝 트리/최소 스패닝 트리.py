import sys
sys.setrecursionlimit(10**5)

vertices_count, edges_count = map(int, sys.stdin.readline().split())

edges = []

for _ in range(edges_count):
    vertex_A, vertex_B, weight = map(int, sys.stdin.readline().split())
    edges.append([vertex_A, vertex_B, weight])

# 각 노드들의 부모 번호를 담을 배열
parent = [i for i in range(vertices_count + 1)]  # [0, 1, 2, 3]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:            # x,y 의 루트가 다르면 각자 다른 트리에 속한 노드들이다.
        parent[y_root] = x_root     # 한쪽을 다른 쪽의 부모로 만들어줌으로써 이 둘을 연결해 준다.
        return True
    return False

edges.sort(key=lambda x: x[2])

mst_weight = 0

for src, dest, weight in edges:
    if union(src, dest):
        mst_weight += weight

print(mst_weight)