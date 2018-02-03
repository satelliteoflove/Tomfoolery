import mobs.mobs
import mobs.mobgroup
import world.world
import world.config
import yaml
import pprint
import os.path

pp = pprint.PrettyPrinter()

class Dm(object):
    """
    """

    def __init__(self):
        """

        """
        self.create_world(world.config.WORLD_CONFIG,
                          world.config.DUNGEON_CONFIG,
                          world.config.LEVEL_CONFIG)
        self.mob_group_list = []

        #Load object templates
        with open(os.path.dirname(__file__) +
                  "/../mobs/moblist.yaml",'r') as self.mob_list_raw:
            self.mob_list = yaml.load(self.mob_list_raw.read())

        with open(os.path.dirname(__file__) +
                  "/../effects/effect_list.yaml",'r') as self.effect_list_raw:
            self.effect_list = yaml.load(self.effect_list_raw.read())

        print(self.effect_list)
        print(self.mob_list)
        self.make_mobgroup(self.mob_list, 3)

    def get_tile_status(self, tile):
        """

        Args:
            tile:

        Returns:

        """
        return getattr(tile, status)
        pass

    def set_tile_status(self, tile):
        """

        Args:
            tile:
        """
        setattr(tile, status, value)
        pass

    def get_party_status(self, party):
        """

        Args:
            party:

        Returns:

        """
        return getattr(party, status)
        pass

    def set_party_status(self, party):
        """

        Args:
            party:
        """
        setattr(party, status, value)
        pass

    def create_world(self, world_config, dungeon_config, level_config):
        """

        Args:
            world_config:
            dungeon_config:
            level_config:
        """
        world1 = world.world.World(world_config,
                                   dungeon_config,
                                   level_config)

    def make_mobgroup(self, mob_list, max_weight):
        """

        Args:
            mob_list:
            max_weight:
        """
        #count = len(self.mob_group_list)
        #dm requests a mob party from a given list (pulled from current dungeon
        #level) and with a given total possible weight.
        mobparty = mobs.mobgroup.MobGroup(mob_list, max_weight)
        print("The following mobs appear:")
        mobparty.list_members()
