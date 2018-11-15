from constants import WHITE, GRAY, BLACK


class Vertex:

    def __init__(self, name, color=WHITE):
        self.name = name
        self.color = color
        self.distance = -1

    def setDistance(self, value):
        self.distance = value

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.distance

    def discover(self):
        self.color = GRAY

    def finish(self):
        self.color = BLACK
