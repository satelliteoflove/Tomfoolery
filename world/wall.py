

class Wall(object):
    """Mutable borders for Tiles.
    
    Keyword arguments:
    walltype -- The type name for the wall (str)."""
    def __init__(self, walltype):
        """

        Args:
            walltype:
        """
        self.name = walltype["name"]
        self.visible = walltype["visible"]
        self.passable = walltype["passable"]
        self.opaque = walltype["opaque"]
        self.closed = walltype["closed"]
        self.description = walltype["description"]
        self.coloring = walltype["coloring"]
