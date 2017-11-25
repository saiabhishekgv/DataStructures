
'''

LeetCode Problem : 127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.


Problem- Transform the word FOOL into the word SAGE. In a word ladder puzzle you must make the change occur gradually by changing one letter at a time.

Explanation:
            POOL
            POLL
            POLE
            PALE
            SALE
            SAGE
'''

from Graph import Graph
from Queue import Queue

def buildGraph(beginWord, dictionary=['hot','dot','dog','lot','log','cog'] ):
    d = {}
    g = Graph()
    for word in dictionary:
        for i in range(len(word)):
            bucket = word[:i]+'_'+word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g

def bfs(g,start):
    if not start:
        return 'No Start point found'
    start.setDistance(0)
    start.setPredecessor(None)
    q = Queue()
    q.put(start)
    while not q.empty():
        currentVertex = q.get()
        for neighbors in currentVertex.getConnections():
            if (neighbors.getColor() == 'white'):
                neighbors.setColor('grey')
                neighbors.setDistance(1+currentVertex.getDistance())
                neighbors.setPredecessor(currentVertex)
                q.put(neighbors)
            currentVertex.setColor('black')

def traverse(y):
    x = y
    while (x.getPredecessor()):
        print(x.getId()),'->',
        x = x.getPredecessor()
    print(x.getId())



g = buildGraph('hit')

for v in g:
    for w in v.getConnections():
        print("( %s , %s ) is an edge with weight %s" % (v.getId(), w.getId(),v.getWeight(w)))


# BFS
start = g.getVertex('hot')
bfs(g,start)
traverse(g.getVertex('cog'))