class Edge:
    player = None
    road = None
    points = None
    edges = None

    def __init__(self, hexes):
        self.hexes = hexes

    def add_points(self, points):
        self.points = points

    def add_edges(self, edges):
        self.edges = edges
