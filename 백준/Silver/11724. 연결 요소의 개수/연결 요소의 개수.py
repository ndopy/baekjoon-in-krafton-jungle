from collections import deque


class Graph:
    def __init__(self, vertices_count):
        self.V = vertices_count
        self.adj = {i: [] for i in range(1, vertices_count + 1)}

    def add_edge(self, src, dest):
        self.adj[src].append(dest)
        self.adj[dest].append(src)

    def bfs(self, starting_vertex):
        visited = set()
        queue = deque()

        visited.add(starting_vertex)
        queue.append(starting_vertex)

        while queue:
            current_vertex = queue.popleft()
            for neighbor_vertex in self.adj[current_vertex]:
                if not neighbor_vertex in visited:
                    visited.add(neighbor_vertex)
                    queue.append(neighbor_vertex)

        return visited

import sys

vertex_count, edge_count = map(int, sys.stdin.readline().split())
graph = Graph(vertex_count)

for _ in range(edge_count):
    source_vertex, target_vertex = map(int, sys.stdin.readline().split())
    graph.add_edge(source_vertex, target_vertex)

visited_set = set()

for i in range(1, vertex_count + 1):
    # 각 정점마다 BFS 해서 방문 결과를 얻고,
    # 그것을 오름차순으로 정렬하여 set 에 넣어서 중복 값을 제거한다.
    # -> 중복이 제거되고 남은 set 안의 아이템 개수가 곧 연결 요소의 개수이다.
    result = graph.bfs(i)
    result = list(result)
    result.sort()

    sorted_tuple = tuple(result)
    visited_set.add(sorted_tuple)

print(len(visited_set))