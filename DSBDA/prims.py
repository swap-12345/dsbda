INF=99999999
V=6
selected_node=[0,0,0,0,0,0]
selected_node[0]=True
no_edge=0
G = [[0, 19, 5, 0, 0,0],
     [19, 0, 5, 9, 2,0],
     [5, 5, 0, 1, 6,0],
     [0, 9, 1, 0, 1,0],
     [0, 3, 6, 1, 0,1],
     [0, 2, 6, 1, 0,0]]

while(no_edge<V-1):
    min=INF
    a = 0
    b = 0
    for m in range(V):
        if selected_node[m]:
            for n in range(V):
                if not selected_node[n] and G[m][n]:
                    if min>G[m][n]:
                        min=G[m][n]
                        a=m
                        b=n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1