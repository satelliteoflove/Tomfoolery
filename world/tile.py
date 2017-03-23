class Tile(object):
    def __init__(self, side_state):
        self.is_explored = False
        self.is_passable = True
        self.characters = []
        self.items = []
