class Point:
    player = None
    settlement = None
    city = None
    edges = []
    def __init__(self, hexes):
        self.hexes = hexes

    def add_edges(self, edges):
        self.edges = edges

    def add_points(self, points):
        self.points = points
