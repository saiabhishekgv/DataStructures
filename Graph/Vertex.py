class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'
        self.distance = 0
        self.predecessor = None

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def getColor(self):
        return self.color

    def setColor(self,newColor):
        self.color = newColor

    def getPredecessor(self):
        return self.predecessor

    def setPredecessor(self,parent):
        self.predecessor = parent

    def getDistance(self):
        return self.distance

    def setDistance(self,  distance):
        self.distance = distance