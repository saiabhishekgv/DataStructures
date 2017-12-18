'''

Finding shortest path of a graph

'''

INF = 999999

def floydWarshal(graph):
    """ dist[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix
    OR we can say that the initial values of shortest distances
    are based on shortest paths considerting no 
    intermedidate vertices """
    dist = map(lambda i: map(lambda j: j, i), graph)
    # dist = [ [i for i in j] for j in graph]
    """ Add all vertices one by one to the set of intermediate
     vertices.
     ---> Before start of a iteration, we have shortest distances
     between all pairs of vertices such that the shortest
     distances consider only the vertices in set 
    {0, 1, 2, .. k-1} as intermediate vertices.
      ----> After the end of a iteration, vertex no. k is
     added to the set of intermediate vertices and the 
    set becomes {0, 1, 2, .. k}
    """

    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                dist[j][k] = min(dist[j][i] + dist[i][k], dist[j][k])
    return dist

graph = [[0,5,INF,10],
         [INF,0,3,INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
        ]

print floydWarshal(graph)