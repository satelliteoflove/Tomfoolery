CONFIG = {
	"dungeon_count": 3,
	"level_count": 3,
	"level_width": 50,
	"level_height": 50
}

class World(object):
	dungeons = []
	def __init__(self, config):
		self.dungeons = [
			Dungeon(config) for x in range(config["dungeon_count"])
		]

class Dungeon(object):
	levels = []
	def __init__(self, config):
		self.levels = [
			Level(config) for x in range(config["level_count"])
		]

class Level(object):
	tiles = []
	def __init__(self, config):
		for x in range(config["level_width"]):
			row = [Tile() for y in range(config["level_height"])]
			self.tiles.append(row)

class Tile(object):
	def __init__(self):
		pass

world =	World(CONFIG)
