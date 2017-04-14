import mobs.mobs
import mobs.mobgroup
import world.world
import world.config
import yaml
import pprint
import os.path

pp = pprint.PrettyPrinter()

class Dm(object):

    def __init__(self):
        self.create_world(world.config.WORLD_CONFIG,
                          world.config.DUNGEON_CONFIG,
                          world.config.LEVEL_CONFIG)
        self.mob_group_list = []
        self.mob_list_raw = open(os.path.dirname(__file__) +
                             "/../mobs/moblist.yaml",'r')
        self.mob_list = yaml.load(self.mob_list_raw.read())
        print(self.mob_list)
        self.make_mobgroup(self.mob_list, 3)

    def get_tile_status(self, tile):
        return getattr(tile, status)
        pass

    def set_tile_status(self, tile):
        setattr(tile, status, value)
        pass

    def get_party_status(self, party):
        return getattr(party, status)
        pass

    def set_party_status(self, party):
        setattr(party, status, value)
        pass

    def create_world(self, world_config, dungeon_config, level_config):
        world1 = world.world.World(world_config,
                                   dungeon_config,
                                   level_config)

    def make_mobgroup(self, mob_list, max_weight):
#        count = len(self.mob_group_list)
        #dm requests a mob party from a given list (pulled from current dungeon
        #level) and with a given total possible weight.
        mobparty = mobs.mobgroup.MobGroup(mob_list, max_weight)
        print("The following mobs exist:")
        pp.pprint(mobparty.members)
