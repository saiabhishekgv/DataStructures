from Graph import Graph
g = Graph()
for i in range(6):
    g.addVertex(i)

print  g.vertList

g.addEdge(0,1,5)
g.addEdge(0,2,9)
g.addEdge(0,3,10)
g.addEdge(0,4,12)
g.addEdge(1,3,1)
g.addEdge(2,4,12)
g.addEdge(2,5,13)
g.addEdge(3,4,15)
g.addEdge(4,5,1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
