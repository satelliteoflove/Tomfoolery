from . import tile
from . import config

class Level(object):
    tiles = []
    def __init__(self, level_config):
        print("Beginning level generation...")
        for x in range(level_config["level_width"]):
            row = [tile.Tile(tile_config["clear"])
                   for y in range(level_config["level_height"])]
            self.tiles.append(row)
        print("Finished level generation.")
