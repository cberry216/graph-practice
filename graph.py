from vertex import Vertex
from constants import TO_VERTEX, FROM_VERTEX, WEIGHT


class Graph:

    def __init__(self, vertices=[], edges=[], directed=False, weighted=False):
        """constructor for Graph class

        Keyword Arguments:
            vertices {list} -- list of string representations of vertices (default: {[]})
            edges {list} -- list of tuples representing edges between vertices (default: {[]})
            directed {bool} -- true if graph is directed, false otherwise (default: {False})
            weighted {bool} -- true if graph is weighted, false otherwise (default: {False})
        """
        self.directed = directed
        self.weighted = weighted
        self.verticesRef = vertices
        self.verticesRef.sort()
        self.vertices = [Vertex(l) for l in vertices]
        self.edges = self.generateAdjacencyMatrix(edges, len(vertices))

    def getVertices(self):
        return self.vertices

    def getVerticesRef(self):
        return self.verticesRef

    def getVertex(self, name):
        return self.vertices[self.indexOf(name)]

    def getVertexNeighbors(self, name):
        adjacent = self.edges[self.indexOf(name)]
        return list(filter(lambda x: adjacent[self.indexOf(x)] == 1, self.verticesRef))

    def getSize(self):
        return len(self.vertices)

    def discoverVertex(self, name):
        self.vertices[self.indexOf(name)].discover()

    def finishVertex(self, name):
        self.vertices[self.indexOf(name)].finish()

    def getColorOfVertex(self, name):
        return self.vertices[self.indexOf(name)].getColor()

    def indexOf(self, name):
        return self.verticesRef.index(name)

    def updateDistance(self, name, value):
        self.vertices[self.indexOf(name)].setDistance(value)

    def updateDiscoverTime(self, name, value):
        self.vertices[self.indexOf(name)].setDiscoverTime(value)

    def updateFinishTime(self, name, value):
        self.vertices[self.indexOf(name)].setFinishTime(value)

    def updateVertexOrigin(self, origin, target):
        self.vertices[self.indexOf(origin)].setOrigin(target)

    def sortVertices(self):
        self.vertices.sort()
        self.verticesRef.sort()

    def generateAdjacencyMatrix(self, edges, numVertices):
        """generates the adjacency matrix given the edges

        Arguments:
            edges {list} -- list of tuples representing edges between vertices
            numVertices {[type]} -- the number of vertices, builds a V x V 2D array

        Returns:
            list -- a 2D array that represents the edges between vertices
        """
        matrix = [[0 for j in range(numVertices)] for i in range(numVertices)]
        for edge in edges:
            value = edge[WEIGHT] if self.weighted else 1
            self.setMatrixValue(matrix, edge[FROM_VERTEX], edge[TO_VERTEX], value)
            if not self.directed:
                self.setMatrixValue(matrix, edge[TO_VERTEX], edge[FROM_VERTEX], value)
        return matrix

    def setMatrixValue(self, matrix, u, v, value):
        """ sets the value located at matrix[u, v] to the given value

        Arguments:
            matrix {list} -- a 2D array that represents the edges between vertices
            u {string} -- the node where the edge originates (unimportant in undirected graph)
            v {string} -- the node where the edge ends (unimportant in undirected graph)
            value {number} -- 1 if the graph is undirected, else the weight to get from u to v
        """
        matrix[self.verticesRef.index(u)][self.verticesRef.index(v)] = value


# vertices = ["D", "C", "B", "A"]
# edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("C", "D")]

# graph = Graph(vertices, edges)
# for v in graph.vertices:
#     print(v.name)
# graph.sortVertices()
# print("sort")
# for v in graph.vertices:
#     print(v.name)
