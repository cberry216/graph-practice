WHITE = "white"
GRAY = "gray"
BLACK = "black"


class Vertex:

    def __init__(self, name, color=WHITE):
        self.name = name
        self.color = color
        self.neighbors = {}

    def setEdge(self, name, weight=1):
        self.neighbors[name] = weight

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def discover(self):
        self.color = GRAY

    def finish(self):
        self.color = BLACK
