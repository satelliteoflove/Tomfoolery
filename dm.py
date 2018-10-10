import world.world
import world.config
import yaml
import pprint
import os.path
import actors.pc
import actors.mobs
import actors.mobgroup
import actors.mobgroup as mg
import actors.config
from actors.items import items
import party.party
import collections
from combat import combat
import curses

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
#        self.current_pc_party.add_char(actors.pc.Character())
        # print(self.effect_list)
        # print(self.mob_list)

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

    def monster_encounter(self):
        """Initiates a monster encounter."""

        # Setting mob party strength.
        strength = len(self.current_pc_party.members) * MOBSTRENGTH
        # Creating a group of mobs from the current list of available mob
        # templates.
        self.current_mobgroup = mg.MobGroup(self.mob_list, strength)

        # These are simply to shorten the variable (list) names in code.
        player_party = self.current_pc_party.members.values()
        mob_group = self.current_mobgroup.members

        if self.current_mobgroup.check_friendly():
            print("They are friendly.")
            print("Do you still attack? (y/n)")
            choice = input()
            if choice == 'y':
                combat.roll_for_initiative(player_party, mob_group)
                battle_grid = combat.build_combat_group(player_party,
                        mob_group)
        else:
            print("They attack!")
            combat.roll_for_initiative(player_party, mob_group)
            # create a list of actors, sort by initiative. Don't over-complicate
            # this! KISS.
            battle_grid = combat.build_combat_group(player_party, mob_group)

    def make_item(self, name):
        """Create item from named template and place in dm's temporary
        queue."""
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
        """Give a PC an item from the active temporary item list."""
        while len(self.item_queue) > 0:
            if len(self.current_pc_party.members) > 0:
                print("Who should receive the item?")
                for actor in self.current_pc_party.members.values():
                    print(actor.name)
            else:
                break
            choice = input()

            for actor in self.current_pc_party.members.values():
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
                k = self.item_queue[choice]
                recipient.get_item(k)
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

    def player_equip(self):
        """Picks equipment for specific player character."""
        print("Which character do you want to equip?")
        for actor in self.current_pc_party.members.values():
            print(actor.name)
        choice = input()
        if self.current_pc_party.members[choice]:
            self.current_pc_party.members[choice].new_equip()
        else:
            print("That character doesn't exist.")

    def view_player(self):
        """Lists active player characters and views information about selected
        player character. Allows interaction with individual characters.
        """
        print("Please choose a player to view.")
        if len(self.current_pc_party.members) > 0:
            for actor in self.current_pc_party.members.values():
                print(actor.name)
            choice = input()
            current_player = self.current_pc_party.members[choice]
            pp.pprint(current_player.return_stats())
        else:
            print("There are no active player characters.")

    def destroy_item(self, player, item):
        """Drop or otherwise destroy item carried by a player."""
        pass

    def menu(self):
        """Prints a list of command options."""
        print("Display this (m)enu.")
        print("Make an (i)tem.")
        print("(g)ive an item.")
        print("(v)iew a player.")
        print("(e)quip a player.")
        print("(c)reate a player.")
        print("e(n)counter mobs.")
        print("(q)uit.")

    def parse_command(self, key):
        """Take string of user input and parse into action."""
        if key == 'i':
            self.make_item("dagger")
        elif key == 'm':
            self.menu()
        elif key == 'g':
            self.give_item()
        elif key == 'c':
            self.current_pc_party.add_char(actors.pc.Character())
        elif key == 'v':
            self.view_player()
        elif key == 'e':
            self.player_equip()
        elif key == 'n':
            self.monster_encounter()
        else:
            return "I have no idea what you're trying to do."
