class Dm(object):

WORLD_CONFIG = {
    "dungeon_count": 1,
    "level_count":1,
    "level_width":4,
    "level_height":4
}


    def __init__(self):
        self.create_world(WORLD_CONFIG)

    def get_tile_status(tile):
        #return getattr(tile, status)
        pass

    def set_tile_status(tile):
        #setattr(tile, status, value)
        pass

    def get_party_status(party):
        #return getattr(party, status)
        pass

    def set_party_status(party):
        #setattr(party, status, value)
        pass

    def create_world(config):
        world = World(config)
