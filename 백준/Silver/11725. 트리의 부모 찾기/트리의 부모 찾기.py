import sys
sys.setrecursionlimit(10**5)

node_count = int(sys.stdin.readline())

class Graph:
    def __init__(self, vertices_count):
        self.V = vertices_count
        self.adj = {i: [] for i in range(1, vertices_count + 1)}
        self.parent = {
            i: None for i in range(1, vertices_count + 1)
        }

    def add_edge(self, src, dest):
        self.adj[src].append(dest)
        self.adj[dest].append(src)

    def dfs(self, start):
        visited = set()

        def visit(v):
            visited.add(v)

            for neighbor in self.adj[v]:
                # 이웃 노드를 아직 방문 안했다면 = v 를 통해 neighbor 를 처음 방문하는 것
                # = 따라서 neighbor 의 부모 노드는 v 가 된다.
                if neighbor not in visited:
                    # 부모 노드를 기록하기
                    self.parent[neighbor] = v

                    visit(neighbor)

        visit(start)

g = Graph(node_count)

for _ in range(node_count - 1):
    start, target = map(int, sys.stdin.readline().split())
    g.add_edge(start, target)

g.dfs(1)

for i in range(2, node_count + 1):
    print(g.parent[i])