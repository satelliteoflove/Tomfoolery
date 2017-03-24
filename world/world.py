from . import dungeon

class World(object):
    dungeons = []
    def __init__(self, world_config, dungeon_config, level_config):
        print("Generating the world...")
        self.dungeons = [
            dungeon.Dungeon(dungeon_config, level_config)
            for x in range(world_config["dungeon_count"])]
        print("Finished world generation.")
