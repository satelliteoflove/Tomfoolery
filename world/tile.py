from . import wall

class Tile(object):
    """A cell on the Level grid.
    
    Each Tile receives configuration data for each Wall, named for direction
    (north, south east, west). Configuration is provided as a dict.
    """
    def __init__(self, north_config, east_config, south_config, west_config,
                coloring):
        self.is_explored = False
        self.is_passable = True
        self.items = []
        self.north = wall.Wall(north_config)
        self.east = wall.Wall(east_config)
        self.south = wall.Wall(south_config)
        self.west = wall.Wall(west_config)
        self.coloring = coloring
