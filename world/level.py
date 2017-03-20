from . import tile

class Level(object):
    tiles = []
    def __init__(self, config):
        print("Beginning level generation...")
        for x in range(config["level_width"]):
            row = [tile.Tile()
                   for y in range(config["level_height"])]
            self.tiles.append(row)
        print("Finished level generation.")
