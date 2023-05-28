class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []
        
    def add_edge(self, u, v, w):
        self.graph.append((w, u, v))
        
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
            
    def kruskal(self):
        result = []
        self.graph.sort()
        parent = list(range(self.V))
        rank = [0] * self.V
        
        for edge in self.graph:
            w, u, v = edge
            if self.find(parent, u) != self.find(parent, v):
                result.append((u, v, w))
                self.union(parent, rank, u, v)
                
        for u, v, weight in result:
            print("Edge:", u, v, "-", weight)

g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 3, 4)
g.add_edge(3, 4, 2)
g.add_edge(4, 5, 6)
g.kruskal()
