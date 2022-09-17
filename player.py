class Player:
    name = None
    bricks = 0
    grain = 0
    lumber = 0
    ore = 0
    wool = 0
    settlements = []
    settlements_left = 5
    cities = []
    cities_left = 4
    roads = []
    long_road = 0
    l_r_points = 0
    roads_left = 15
    large_army = 0
    l_a_points = 0
    knight_cards = 0
    progress_cards = 0
    v_points_cards = 0

    def __init__(self, name):
        self.name = name