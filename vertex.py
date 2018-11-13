WHITE = "white"
GRAY = "gray"
BLACK = "black"


class Vertex:

    def __init__(self, name, color=WHITE):
        self.name = name
        self.color = color

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def discover(self):
        self.color = GRAY

    def finish(self):
        self.color = BLACK
