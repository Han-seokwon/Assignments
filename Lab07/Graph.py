


class Edge:
    def __init__(self, u=None, v=None, weight=None):
        self.u = u
        self.v = v
        self.weight = weight

    def __str__(self):
        return "({}, {}) -> {} ".format(self.u, self.v, self.weight)
    def __repr__(self):
        return "({}, {}) -> {} ".format(self.u, self.v, self.weight)
    def __hash__(self):
        return hash(self.weight)
    def __eq__(self, other):
        return self.weight == other.weight
    def __ne__(self, other):
        return self.weight != other.weight
    def __lt__(self, other):
        return self.weight < other.weight
    def __le__(self, other):
        return self.weight <= other.weight
    def __gt__(self, other):
        return self.weight > other.weight
    def __ge__(self, other):
        return self.weight >= other.weight
class Vertex: # Node
    def __init__(self, key=None):
        self.key = key

    def __str__(self):
        return str(self.key)
    def __repr__(self):
        return str(self.key)
    def setData(self, key):
        self.key = key

    def getData(self, key):
        return self.key
    def __hash__(self):
        return hash(self.key)
    def __eq__(self, other):
        return self.key == other.key
    def __ne__(self, other):
        return self.key != other.key
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key <= other.key
    def __gt__(self, other):
        return self.key > other.key
    def __ge__(self, other):
        return self.key >= other.key


class Graph:
    def __init__(self):
        pass
















