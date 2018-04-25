import mobs.mobs 
import mobs.mobgroup
import world.world
import world.config
import yaml
import pprint
import os.path
import characters.pc
import characters.config

pp = pprint.PrettyPrinter()


class Dm(object):
    def __init__(self):
        self.create_world(world.config.WORLD_CONFIG,
                          world.config.DUNGEON_CONFIG,
                          world.config.LEVEL_CONFIG)
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
 
        self.make_mobgroup(self.mob_list, 3)

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

    def make_mobgroup(self, mob_list, max_weight):
        """Create group of mobs from "mob_list" with a maximum party weight of
        "max_weight"."""
        #count = len(self.mob_group_list)
        #dm requests a mob party from a given list (pulled from current dungeon
        #level) and with a given total possible weight.
        mobparty = mobs.mobgroup.MobGroup(mob_list, max_weight)
        print("The following mobs appear:")
        mobparty.list_members()

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

# Re-implementing command parser. commands are passed to the dm,
# and the dm handles the actions and actors.
    def monster_encounter(self, mobgroup):
        pass

    def give_item(self, player, item):
        pass

    def destroy_item(self, player, item):
        pass

    def show_inventory(self, player):
        pass

    def parse_command(self, move):
        """Take string of user input and parse into action."""
        if move[0] == "encounter":
            self.monster_encounter(self.make_mobgroup(self.mob_list, 3))
#        elif move[0] == "get" or move[0] == "take":
#            player.get(move[1])
#        elif move[0] == "inventory":
#            player.show_inventory()
#        elif move[0] == "equip":
#            player.equip(move[1])
#        elif move[0] == "drop":
#            player.drop(move[1])
#        elif move[0] == "look":
#            player.view_surroundings()
#        elif move[0] == "attack" and move[1]:
#            player.attack(move[1])
#        elif move[0] == "look":
#            player.view_surroundings()
#        elif move[0] == "status":
#            player.show_stats()
#        elif move[0] == "addxp":
#            player.add_xp(int(move[1]))
#        elif move[0] == "levelup":
#            player.level_up()
#        elif move[0] == "help":
#            showInstructions()
#            dir(player)
#        elif move[0] == "bonuspoints":
#            player.bonusPoints = int(move[1])
#        elif move[0] == "classchange":
#            player.set_class()
#        else:
           # print("I have no idea what you're trying to do.")
