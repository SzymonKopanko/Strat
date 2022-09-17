class Hexagon:
    type = None
    number = None
    resource = None

    def __init__(self, type, number, resource):
        self.type = type
        if type == "land":
            self.number = number
            self.resource = resource

    def return_resource(self, player):
        if self.resource == "bricks":
            player.bricks += 1
        elif self.resource == "grain":
            player.grain += 1
        elif self.resource == "lumber":
            player.lumber += 1
        elif self.resource == "ore":
            player.ore += 1
        elif self.resource == "wool":
            player.wool += 1
