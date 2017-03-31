import mobs.mobgroup
import yaml

class Dm(object):

    def __init__(self):
        #self.create_world(WORLD_CONFIG)
        self.mob_group_list = []
        self.mob_list = yaml.load(open("mobs/moblist.yaml","r"))
        self.make_mobgroup()

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

    def make_mobgroup(self):
        count = len(self.mob_group_list)
        mobparty = mobs.mobgroup.MobGroup(1, self.mob_list, count)
        self.mob_group_list.append(mobparty)
