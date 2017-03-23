from config import WALL_TYPES

class Wall(object):
    """Mutable borders for Tiles.
    
    Keyword arguments:
    walltype -- The type name for the wall (str)."""
    def __init__(self, walltype):
        self.name = WALL_TYPES[WALL_TYPES[walltype]]["name"]
        self.visible = WALL_TYPES[walltype]["visible"]
        self.passable = WALL_TYPES[walltype]["passable"]
        self.opaque = WALL_TYPES[walltype]["opaque"]
        self.closed = WALL_TYPES[walltype]["closed"]
        self.description = WALL_TYPES[walltype]["description"]
        self.coloring = WALL_TYPES[walltype]["coloring"]
