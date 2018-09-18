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
        #Setting mob party strength.
        strength = len(self.current_pc_party.members) * MOBSTRENGTH
        #Creating a 'current_mobgroup'.
        self.current_mobgroup = actors.mobgroup.MobGroup(self.mob_list,
                strength)
        #Populating 'a' with party members.
        a = self.current_pc_party.members.values()
        #Populating 'b' with mob members.
        b = self.current_mobgroup.members

        #print("Are they friendly?")
        if self.current_mobgroup.check_friendly():
            print("They are friendly.")
        else:
            print("They attack!")
            combat.roll_for_initiative(a, b)
            #create a list of actors, sort by initiative.
            combatants = combat.build_combat_group(a, b)

    def make_item(self, name):
        """Create item from named template and place in dm's temporary queue."""
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
        print("Enter one of the following:")
        print("(m)ake an item.")
        print("(g)ive an item.")
        print("(v)iew a player.")
        print("(e)quip a player.")

    def parse_command(self, key):
        """Take string of user input and parse into action."""
        self.menu()
        #if key == curses.KEY_DOWN:
        #    cursor_y = cursor_y + 1
        #elif key == ord('e'):
        #    self.monster_encounter()
        #elif key == ord('p'):
        #    self.current_pc_party.add_char(actors.pc.Character())
        if move[0] == "mkitem":
            self.make_item("dagger")
        elif move[0] == "gvitem":
            self.give_item()
        elif move[0] == "view":
            self.view_player()
        elif move[0] == "equip":
            self.player_equip()
        else:
            return "I have no idea what you're trying to do."
