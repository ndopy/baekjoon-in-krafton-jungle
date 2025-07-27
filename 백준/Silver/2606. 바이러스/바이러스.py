import sys

class Graph:
    def __init__(self, vertices_count):
        self.V = vertices_count
        self.adjacent_vertices = {i: [] for i in range(1, vertices_count + 1)}

    def add_edge(self, source_vertex, target_vertex):
        self.adjacent_vertices[source_vertex].append(target_vertex)
        self.adjacent_vertices[target_vertex].append(source_vertex)

    def dfs(self, starting_vertex):
        # print(f'DFS 탐색 시작 (시작 노드 : {starting_vertex})')
        visited = set()

        def visit(current_vertex):
            # print(f'현재 노드 : {current_vertex}')
            visited.add(current_vertex)

            for neighbor_vertex in self.adjacent_vertices[current_vertex]:
                if not neighbor_vertex in visited:
                    visited.add(neighbor_vertex)
                    visit(neighbor_vertex)

        visit(starting_vertex)
        # print(f'DFS 탐색 종료')
        return visited


computer_count = int(sys.stdin.readline())
edge_count = int(sys.stdin.readline())

graph = Graph(computer_count)


for _ in range(edge_count):
    src_vertex, dest_vertex = list(map(int, sys.stdin.readline().split()))
    graph.add_edge(src_vertex, dest_vertex)

visited_vertices = graph.dfs(1)
print(len(visited_vertices) - 1)



