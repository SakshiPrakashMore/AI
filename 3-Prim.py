import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_algo(self):
        key = [sys.maxsize] * self.V
        parent = [-1] * self.V
        mst_set = [False] * self.V
        
        key[0] = 0
        
        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True
            
            for v, w in self.graph[u]:
                if not mst_set[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u
        
        self.print_mst(parent)

    def min_key(self, key, mst_set):
        min_val = sys.maxsize
        min_index = -1
        
        for v in range(self.V):
            if key[v] < min_val and not mst_set[v]:
                min_val = key[v]
                min_index = v
        
        return min_index

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.get_weight(parent[i], i))
    
    def get_weight(self, u, v):
        for vertex, weight in self.graph[u]:
            if vertex == v:
                return weight
        return None

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
g.prim_algo()