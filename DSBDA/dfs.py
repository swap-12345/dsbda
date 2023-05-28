graph={
    '0':['1','2','3'],
    '1':['0','4'],
    '2':['0','3','4'],
    '3':['0','3','5'],
    '4':['2','1'],
    '5':['3']
}
visited=set()
def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print('Depth first search')
dfs(visited,graph,'0')