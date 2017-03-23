from . import config

class Wall(object):
    """Mutable borders for Tiles.
    
    Keyword arguments:
    walltype -- The type name for the wall (str)."""
    def __init__(self, walltype):
        self.name = config.WALL_TYPES[walltype]["name"]
        self.visible = config.WALL_TYPES[walltype]["visible"]
        self.passable = config.WALL_TYPES[walltype]["passable"]
        self.opaque = config.WALL_TYPES[walltype]["opaque"]
        self.closed = config.WALL_TYPES[walltype]["closed"]
        self.description = config.WALL_TYPES[walltype]["description"]
        self.coloring = config.WALL_TYPES[walltype]["coloring"]
