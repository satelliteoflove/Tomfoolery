import mobs.mobs 
import mobs.mobgroup
from mobs import mobs
from mobs import mobgroup
import world.world
import world.config
import yaml
import pprint
import os.path
import characters.pc
import characters.config
import party

pp = pprint.PrettyPrinter()


class Dm(object):
    def __init__(self):
#        self.create_world(world.config.WORLD_CONFIG,
#                          world.config.DUNGEON_CONFIG,
#                          world.config.LEVEL_CONFIG)
        self.mob_group_list = []

        self.carry_over = 0
        # Load object templates
        with open(os.path.dirname(__file__) +
                  "/mobs/moblist.yaml", 'r') as self.mob_list_raw:
            self.mob_list = yaml.load(self.mob_list_raw.read())

        with open(os.path.dirname(__file__) +
                  "/effects/effect_list.yaml", 'r') as self.effect_list_raw:
            self.effect_list = yaml.load(self.effect_list_raw.read())

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
        new_player = characters.pc.Character()

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
        pass



# Re-implementing command parser. commands are passed to the dm,
# and the dm handles the actions and actors.
    def monster_encounter(self):
        strength = len(self.current_pc_party.members) * 1.5
        self.current_mobgroup = mobgroup.MobGroup(self.mob_list, strength)
        self.current_mobgroup.list_members()

        if self.current_mobgroup.check_friendly():
            print("They are friendly.")
        else:
            print("They attack!")

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
        elif move[0] == "makepc":
            self.make_pc()
        elif move[0] == "mkparty":
            self.current_pc_party = party.party.Party()
        elif move[0] == "mkpc":
            self.current_pc_party.add_char(characters.pc.Character())
        else:
            print("I have no idea what you're trying to do.")
