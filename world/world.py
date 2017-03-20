from . import dungeon

class World(object):
    dungeons = []
    def __init__(self, config):
        print("Generating the world...")
        self.dungeons = [
            dungeon.Dungeon(config)
            for x in range(config["dungeon_count"])]
        print("Finished world generation.")
