from . import level

class Dungeon(object):
    levels = []
    def __init__(self, config):
        print("Beginning dungeon generation...")
        self.levels = [
            level.Level(config)
            for x in range(config["level_count"])]
        print("Finished dungeon generation.")
