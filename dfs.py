from constants import WHITE
from graph import Graph

TIME = 0


def dfs(graph):
    # d = [-1 for i in range(graph.getSize())]
    # f = [-1 for i in range(graph.getSize())]
    # pi = [-1 for i in range(graph.getSize())]
    global TIME
    TIME = 0
    # graph.sortVertices()
    print(graph.getVerticesRef())
    for vertex in graph.getVerticesRef():
        if graph.getColorOfVertex(vertex) is WHITE:
            dfsVisit(graph, vertex)


def dfsVisit(graph, vertex):
    global TIME
    graph.discoverVertex(vertex)
    TIME += 1
    graph.updateDiscoverTime(vertex, TIME)
    for neighbor in graph.getVertexNeighbors(vertex):
        if graph.getColorOfVertex(neighbor) is WHITE:
            graph.updateVertexOrigin(neighbor, vertex)
            dfsVisit(graph, neighbor)
    graph.finishVertex(vertex)
    TIME += 1
    graph.updateFinishTime(vertex, TIME)


vertices = ["Y", "W", "S", "T", "X", "Z", "U", "V"]
edges = [("Y", "X"), ("W", "Y"), ("X", "W"), ("Z", "X"), ("W", "Z"), ("S", "W"),
         ("S", "Z"), ("U", "Z"), ("U", "S"), ("T", "U"), ("V", "U"), ("T", "V"), ("V", "T")]

graph = Graph(vertices, edges, directed=True)

dfs(graph)

for vertex in graph.getVertices():
    print(vertex.getName() + ".time : " + str(vertex.getDiscoverTime()) +
          "\t" + str(vertex.getFinishTime()) + "\t" + vertex.getOrigin())
