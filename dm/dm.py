import mobs
import mobs.mobgroup
import yaml
import pprint

pp = pprint.PrettyPrinter()

class Dm(object):

    def __init__(self):
        #self.create_world(WORLD_CONFIG)
        self.mob_group_list = []
        self.mob_list = yaml.load(open("mobs/moblist.yaml","r"))
        self.make_mobgroup()

    def get_tile_status(tile):
        return getattr(tile, status)
        pass

    def set_tile_status(tile):
        setattr(tile, status, value)
        pass

    def get_party_status(party):
        return getattr(party, status)
        pass

    def set_party_status(party):
        setattr(party, status, value)
        pass

    def create_world(config):
        world = World(config)

    def get_candidate_mob(self, mob_list):
        mobs.Mob(mob_list)

    def make_mobgroup(self):
#        count = len(self.mob_group_list)
        mobparty = mobs.mobgroup.MobGroup()
        mobparty.remaining_weight = 2
        mobparty.add_mob(mobs.mobs.Mob(
        self.mob_group_list.append(mobparty)
        print("The following mobs exist:")
        pp.pprint(mobparty.members)
