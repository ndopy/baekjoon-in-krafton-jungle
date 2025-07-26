import sys
from collections import deque

sys.setrecursionlimit(10**5)

class Graph:
    def __init__(self, vertices_count):
        self.V = vertices_count
        self.adjacent_vertices = {i: [] for i in range(1, vertices_count + 1)}

    def add_edge(self, source_vertex, target_vertex):
        self.adjacent_vertices[source_vertex].append(target_vertex)
        self.adjacent_vertices[target_vertex].append(source_vertex)

    def dfs(self, starting_vertex):
        visited = set()

        def visit(current_vertex):
            visited.add(current_vertex)
            print(f'{current_vertex}', end=' ')

            # 이웃 정점 목록을 sort
            current_adjacent = self.adjacent_vertices[current_vertex]
            current_adjacent.sort()

            for neighbor_vertex in current_adjacent:
                if not neighbor_vertex in visited:
                    visited.add(neighbor_vertex)
                    visit(neighbor_vertex)

        visit(starting_vertex)

    def bfs(self, starting_vertex):
        visited = set()
        queue = deque()

        visited.add(starting_vertex)
        queue.append(starting_vertex)

        while queue:
            current_vertex = queue.popleft()
            print(f'{current_vertex}', end=' ')

            # 이웃 정점 목록을 sort
            current_adjacent = self.adjacent_vertices[current_vertex]
            current_adjacent.sort()

            for neighbor_vertex in self.adjacent_vertices[current_vertex]:
                if not neighbor_vertex in visited:
                    visited.add(neighbor_vertex)
                    queue.append(neighbor_vertex)


v_count, e_count, starting_vertex = map(int, sys.stdin.readline().split())

# 그래프 생성
graph = Graph(v_count)

# 간선 생성
for _ in range(e_count):
    src, dest = map(int, sys.stdin.readline().split())
    graph.add_edge(src, dest)

# DFS 수행 결과
graph.dfs(starting_vertex)

print()

# BFS 수행 결과
graph.bfs(starting_vertex)