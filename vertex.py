from constants import WHITE, GRAY, BLACK


class Vertex:

    def __init__(self, name, color=WHITE):
        self.name = name
        self.color = color
        self.distance = -1
        self.discoverTime = -1
        self.finishTime = -1
        self.origin = ""

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __lt__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def setDistance(self, value):
        self.distance = value

    def setDiscoverTime(self, value):
        self.discoverTime = value

    def setFinishTime(self, value):
        self.finishTime = value

    def setOrigin(self, value):
        self.origin = value

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.distance

    def getDiscoverTime(self):
        return self.discoverTime

    def getFinishTime(self):
        return self.finishTime

    def getOrigin(self):
        return self.origin

    def discover(self):
        self.color = GRAY

    def finish(self):
        self.color = BLACK
