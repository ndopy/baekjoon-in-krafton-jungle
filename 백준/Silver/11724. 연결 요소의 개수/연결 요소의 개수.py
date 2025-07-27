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
connection_count = 0

for vertex in range(1, vertex_count + 1):
    if vertex in visited_set:
        continue

    bfs_result = graph.bfs(vertex)
    visited_set.update(bfs_result)
    connection_count += 1

print(connection_count)