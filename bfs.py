from queue import Queue
from constants import WHITE
from graph import Graph


def bfs(graph, start):
    queue = Queue()

    graph.discoverVertex(start)
    queue.put((start, 0))

    while queue.empty() is not True:
        currentVertex, vertexDist = queue.get()

        graph.finishVertex(currentVertex)
        graph.updateDistance(currentVertex, vertexDist)

        neighbors = graph.getVertexNeighbors(currentVertex)
        for n in neighbors:
            if graph.getColorOfVertex(n) is WHITE:
                graph.discoverVertex(n)
                queue.put((n, vertexDist + 1))


vertices = ["W", "S", "T", "U", "V", "R", "X", "Y"]
edges = [("W", "S"), ("W", "V"), ("S", "R"), ("R", "T"), ("R", "X"), ("T", "X"), ("T", "U"), ("X", "Y"), ("U", "Y")]

graph = Graph(vertices, edges)

bfs(graph, "S")
for v in graph.vertices:
    print(v.getName() + ".distance : " + str(v.getDistance()))
