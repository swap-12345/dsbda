from numpy import Inf
def Dijkstra(graph, start):
    l = len(graph)
    dist = [Inf for i in range(l)]
    dist[start] = 0
    vis = [False for i in range(l)]
    for i in range(l):        
        u = -1        
        for x in range(l):
            if not vis[x] and (u == -1 or dist[x] < dist[u]):
                u = x
                
        if dist[u] == Inf:
            break
            
        vis[u] = True
        
        for v, d in graph[u]:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                
    return dist

graph = {
    0: [(1, 1),(5,5)],
    1: [(0, 1), (2, 2), (3, 3)],
    2: [(1, 2), (3, 1), (4, 5)],
    3: [(1, 3), (2, 1), (4, 1)],
    4: [(2, 5), (3, 1),(1,5)],
    5:[(1,4)]
}
print(Dijkstra(graph,0))