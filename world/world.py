from . import dungeon

class World(object):
    dungeons = []
    def __init__(self, world_config):
        print("Generating the world...")
        self.dungeons = [
            dungeon.Dungeon(world_config)
            for x in range(world_config["dungeon_count"])]
        print("Finished world generation.")
