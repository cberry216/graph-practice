from vertex import Vertex

# Edge index constants
FROM_VERTEX = 0
TO_VERTEX = 1
WEIGHT = 2


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
        self.vertexMap = vertices
        self.vertices = {l: Vertex(l) for l in vertices}
        self.generateEdges(edges)

    def generateEdges(self, edges):
        for edge in edges:
            if not self.weighted:
                self.vertices[edge[FROM_VERTEX]].setEdge(edge[TO_VERTEX])
                if not self.directed:
                    self.vertices[edge[TO_VERTEX]].setEdge(edge[FROM_VERTEX])
            else:
                self.vertices[edge[FROM_VERTEX]].setEdge(edge[TO_VERTEX], edge[WEIGHT])
                if not self.directed:
                    self.vertices[edge[TO_VERTEX]].setEdge(edge[FROM_VERTEX], edge[WEIGHT])
    # def generateAdjacencyMatrix(self, edges, numVertices):
    #     """generates the adjacency matrix given the edges

    #     Arguments:
    #         edges {list} -- list of tuples representing edges between vertices
    #         numVertices {[type]} -- the number of vertices, builds a V x V 2D array

    #     Returns:
    #         list -- a 2D array that represents the edges between vertices
    #     """
    #     matrix = [[0 for j in range(numVertices)] for i in range(numVertices)]
    #     for edge in edges:
    #         value = edge[WEIGHT] if self.weighted else 1
    #         self.setMatrixValue(
    #             matrix, edge[FROM_VERTEX], edge[TO_VERTEX], value)
    #         if not self.directed:
    #             self.setMatrixValue(
    #                 matrix, edge[TO_VERTEX], edge[FROM_VERTEX], value)
    #     return matrix

    # def setMatrixValue(self, matrix, u, v, value):
    #     """ sets the value located at matrix[u, v] to the given value

    #     Arguments:
    #         matrix {list} -- a 2D array that represents the edges between vertices
    #         u {string} -- the node where the edge originates (unimportant in undirected graph)
    #         v {string} -- the node where the edge ends (unimportant in undirected graph)
    #         value {number} -- 1 if the graph is undirected, else the weight to get from u to v
    #     """
    #     matrix[self.vertRef.index(u)][self.vertRef.index(v)] = value


vertices = ["A", "B", "C", "D"]
edges = [("A", "B"), ("A", "C"), ("A", "D"), ("B", "C"), ("C", "D")]

graph = Graph(vertices, edges)
print(graph.vertices["A"].neighbors)
print(graph.vertices["B"].neighbors)
print(graph.vertices["C"].neighbors)
print(graph.vertices["D"].neighbors)
print(graph.vertices["E"])
