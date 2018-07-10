import world.world
import world.config
import yaml
import pprint
import os.path
import actors.pc
import actors.mobs
import actors.mobgroup
import actors.config
from actors.items import items
import party.party
from operator import attrgetter
import collections

pp = pprint.PrettyPrinter()

# Constants
MOBSTRENGTH = 1.5

class Dm(object):
    def __init__(self):
#        self.create_world(world.config.WORLD_CONFIG,
#                          world.config.DUNGEON_CONFIG,
#                          world.config.LEVEL_CONFIG)
        self.mob_group_list = {}

        self.carry_over = 0
        # Load object templates
        with open(os.path.dirname(__file__) +
                  "/actors/moblist.yaml", 'r') as self.mob_list_raw:
            self.mob_list = yaml.load(self.mob_list_raw.read())

        with open(os.path.dirname(__file__) +
                "/actors/items/item_list.yaml", 'r') as self.item_config_raw:
            self.item_config = yaml.load(self.item_config_raw.read())

        # Initialize temporary item queue.
        self.item_queue = {}
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
#            for actor in combatants:
#                print(actor.name + " init = " + str(actor.initiative) + ".")
#                if actor.type:
#                    print(actor.name + " has a type of: " + actor.type + ".")
#                    pass

    def make_item(self, name):
        if self.item_config[name]:
            new_item = items.Item(self.item_config[name])
            self.item_queue[new_item.name +
                    str(len(self.item_queue) + 1)] = new_item
            for k in self.item_queue.keys():
                print(k)
            print(new_item.name + " has been added to the queue.")
#            print(vars(new_item))
        else:
            print("No item pattern matching that name exists.")

    def give_item(self):

        while len(self.item_queue) > 0:
            print("Who should receive the item?")
            for actor in self.current_pc_party.members:
                print(actor.name)
            choice = input()

            for actor in self.current_pc_party.members:
                if choice == actor.name:
                    recipient = actor
                    print(recipient.name + " will get the item.")
                else:
                    print("That recipient doesn't exist.")

            print("Which item should " + actor.name + " receive?")
            for k in self.item_queue.keys():
                print(k)
            choice = input()

            if self.item_queue[choice]:
                recipient.inventory.append(self.item_queue[choice])
                self.item_queue.__delitem__(choice)
            else:
                print("That item doesn't exist.")

            if len(self.item_queue) > 0:
                print("Items remain. Do you want to take them?")
                choice = input()
                if choice == "y" or choice == "yes":
                    self.give_item()
                elif choice == "n" or choice == "no":
                    print("Clearing the queue.")
                    self.item_queue.clear()

    def view_player(self):
        """Lists active player characters and views information about selected
        player character.
        """
        pass


    def destroy_item(self, player, item):
        """Drop or otherwise destroy item carried by a player."""
        pass

    def show_inventory(self):
        """Show what a specific player is carrying, including equipped items.
        :player: Must be from the dm's current_pc_party.
        """
        print("Which player's inventory do you want to see?")
        for actor in current_pc_party.members:
            print(actor.name)
        print(player.name + " is carrying the following:")
        for item in player.inventory:
            print(item.name)

    def parse_command(self, move):
        """Take string of user input and parse into action."""
        if move[0] == "enc":
            self.monster_encounter()
        elif move[0] == "mkpc":
            self.current_pc_party.add_char(actors.pc.Character())
        elif move[0] == "mkitem":
            self.make_item("dagger")
        elif move[0] == "gvitem":
            self.give_item()
        elif move[0] == "view":
            self.view_player()
        else:
            print("I have no idea what you're trying to do.")
