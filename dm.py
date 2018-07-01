import actors.mobs
import actors.mobgroup
import world.world
import world.config
import yaml
import pprint
import os.path
import actors.pc
import actors.config
import party.party
from operator import attrgetter

pp = pprint.PrettyPrinter()

# Constants
MOBSTRENGTH = 1.5

class Dm(object):
    def __init__(self):
#        self.create_world(world.config.WORLD_CONFIG,
#                          world.config.DUNGEON_CONFIG,
#                          world.config.LEVEL_CONFIG)
        self.mob_group_list = []

        self.carry_over = 0
        # Load object templates
        with open(os.path.dirname(__file__) +
                  "/actors/moblist.yaml", 'r') as self.mob_list_raw:
            self.mob_list = yaml.load(self.mob_list_raw.read())

        with open(os.path.dirname(__file__) +
                "/actors/items/item_list.yaml", 'r') as self.item_config_raw:
            self.item_config = yaml.load(self.item_config_raw.read())

        self.current_pc_party = party.party.Party()
        # print(self.effect_list)
        # print(self.mob_list)

    def get_tile_status(self, tile):
        # return getattr(tile, status)
        pass

    def set_tile_status(self, tile):
        # setattr(tile, status, value)
        pass

    def get_party_status(self, party):
        # return getattr(party, status)
        pass

    def set_party_status(self, party):
        # setattr(party, status, value)
        pass

    def make_npc(self):
        """Create Non-Player Character, taking input file."""
        pass

    def make_pc(self):
        """Create Player Character and run through generation."""
        new_player = actors.pc.Character()

    def create_world(self, world_config, dungeon_config, level_config):
        world1 = world.world.World(world_config,
                                   dungeon_config,
                                   level_config)

    def is_encounter(self, tile):
        """Determine if party encounters mobs. Return True/False."""
        # what is the base_chance for the current level?
        # currently, every encounter is guaranteed.
        # base_chance = tile.base_chance
        carry_over = self.carry_over
        base_chance = 100.0
        if base_chance + carry_over <= 100.0:
            # self.carry_over = carry_over + tile_carry_increment
            return False
        elif base_chance + carry_over >= 100.0:
            self.carry_over = 0
            return True

    def roll_for_initiative(self, party, mobgroup):
        for actor in party:
            actor.roll_init()
#            print("initiative for " + actor.name +
#                  " is " + str(actor.initiative) + ".")
        for actor in mobgroup:
            actor.roll_init()
#            print("initiative for " + actor.name +
#                  " is " + str(actor.initiative) + ".") 

    def monster_encounter(self):
        strength = len(self.current_pc_party.members) * MOBSTRENGTH
        self.current_mobgroup = actors.mobgroup.MobGroup(self.mob_list,
                strength)
#        self.current_mobgroup.list_members()

        if self.current_mobgroup.check_friendly():
            print("They are friendly.")
        else:
            print("They attack!")
            self.roll_for_initiative(self.current_pc_party.members,
                                     self.current_mobgroup.members)
            #create a list of actors, sort by initiative.
            combatants = []
            for actor in self.current_pc_party.members:
                combatants.append(actor)
            for actor in self.current_mobgroup.members:
                combatants.append(actor)
            combatants.sort(key = attrgetter('initiative'))
            for actor in combatants:
                print(actor.name + " init = " + str(actor.initiative) + ".")
                if actor.type:
                    print(actor.name + " has a type of: " + actor.type + ".")

    def make_item(self, config):
        """Make an item from the list.

        :config: TODO
        :returns: TODO

        """
        pass

    def give_item(self, player, item):
        pass

    def destroy_item(self, player, item):
        """Drop or otherwise destroy item carried by a player."""
        pass

    def show_inventory(self, player):
        """Show what a specific player is carrying, including equipped items."""
        pass

    def parse_command(self, move):
        """Take string of user input and parse into action."""
        if move[0] == "enc":
            self.monster_encounter()
        elif move[0] == "mkpc":
            self.current_pc_party.add_char(actors.pc.Character())
        else:
            print("I have no idea what you're trying to do.")
