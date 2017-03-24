from . import level
from . import config

class Dungeon(object):
    levels = []
    def __init__(self, dungeon_config, level_config):
        print("Beginning dungeon generation...")
        self.levels = [
            level.Level(level_config)
            for x in range(dungeon_config["level_count"])]
        print("Finished dungeon generation.")
