from . import wall

class Tile(object):
    """A cell on the Level grid.
    
    Each Tile receives configuration data for each Wall, named for direction
    (north, south east, west). Configuration is provided as a dict.
    """
    #TODO: God what an unholy mess...
    #def __init__(self, north_config, east_config, south_config, west_config,
    #           coloring):
    def __init__(self, tile_config):
        """

        Args:
            tile_config:
        """
        self.is_explored = False
        self.is_passable = True
        self.items = []
        self.north = wall.Wall(tile_config)
        self.east = wall.Wall(tile_config)
        self.south = wall.Wall(tile_config)
        self.west = wall.Wall(tile_config)
        self.tile_char = tile_config["tile_char"]
        self.base_chance = 0.0
