__author__ = 'Chris'

import random
import struct

# Globals
world_characters = []
MAP_WIDTH = 0
MAP_HEIGHT = 0

# Character levels (universal)
# Note that experience required to gain a level are based on a combination of
# character class and character race. All races gain levels in different classes
# at different rates. 28 different rates are applied, with the lowest
# requirement at rate 1 and the highest requirement at 28.



char_level_xp_req = {
    1:{2:750,
       3:833,
       4:1055,
       5:1758,
       6:2930,
       7:4884,
       8:8140,
       9:13566,
       10:22610,
       11:37684,
       12:62806,
       13:104677,
       14:211693
      }
}

char_level_xp_rate = {
    "human":{"fighter":4,
             "mage":5,
             "priest":5,
             "thief":7,
             "alchemist":11,
             "bishop":15,
             "bard":7,
             "ranger":4,
             "psionic":14,
             "valkyrie":10,
             "samurai":14,
             "lord":24,
             "monk":16,
             "ninja":28}
}

# TODO: Add other races to list following table in characters.md.


class Character(object):
    """Common base class for all PCs and NPCs."""

    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.current_level = 1
        self.current_xp = 0
        self.rate = 1
        self.char_class = "fighter"
        self.race = "human"
        self.sex = "male"
        self.strength = 8
        self.vitality = 8
        self.hitPoints = int((self.vitality / 10) * random.randint(5, 30))
        self.attack = 1
        self.bonusPoints = random.randint(5, 25)
        self.defense = 1
        self.inventory = []
        self.currentRoom = (0, 0)
        self.add_to_room()
        self.direction = "north"
        world_characters.append(self)
        self.equipment = []

    def add_to_room(self):
        for chamber in rooms:
            if chamber == self.currentRoom:
                rooms[self.currentRoom]["characters"].append(self)

    def show_stats(self):
        print(vars(self))

    def show_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.is_equipped == True:
                    print("#" + item.name)
                else:
                    print(item.name)
        else:
            print("You aren't carrying anything.")
            # list items, none if empty


    def place_random(self):
        # start the player off in a room
        self.currentRoom = random.randrange()

    def place_room(self, room: int):
        if room > 0 and room <= len(rooms):
            self.currentRoom = room

    def view_surroundings(self):
        """print what the player can see"""
        currentRoom = self.currentRoom
        current_room_character_list = []
        print("===================")
        print("You are in the " + rooms[currentRoom]["name"])
        if "description" in rooms[currentRoom]:
            print(rooms[currentRoom]["description"])
        if "items" in rooms[currentRoom]:
            for thing in rooms[currentRoom]["items"]:
                print("In the room, you see a " + thing.name + ".")
        for room_character in rooms[self.currentRoom]["characters"]:
            current_room_character_list.append(room_character)
        print("Nearby, you see " + str(len(current_room_character_list)) + " characters:")
        for character in current_room_character_list:
            print(character.name)
        print("Exits:")
        if "north" in rooms[currentRoom]:
            print("North")
        if "south" in rooms[currentRoom]:
            print("South")
        if "east" in rooms[currentRoom]:
            print("East")
        if "west" in rooms[currentRoom]:
            print("West")

    def go(self, newroom):
        if move[1] in rooms[self.currentRoom]:
            rooms[self.currentRoom]["characters"].remove(self)
            self.currentRoom = rooms[self.currentRoom][move[1]]
            rooms[self.currentRoom]["characters"].append(self)
            self.view_surroundings()
        else:
            print("You can't go that way.")

    def get(self, item_to_get):
        temp_item_list = []
        for item in rooms[self.currentRoom]["items"]:
            temp_item_list.append(item.name)
        if "items" in rooms[self.currentRoom] and item_to_get in temp_item_list:
            for item in rooms[self.currentRoom]["items"]:
                if item_to_get == item.name:
                    self.inventory.append(item)
                    print(item.name + " taken.")
                    rooms[self.currentRoom]["items"].remove(item)
        else:
            print("You can't take " + item_to_get + ".")

    def drop(self, item_to_drop):
        temp_item_list = []
        for item in self.inventory:
            temp_item_list.append(item.name)
        if item_to_drop in temp_item_list:
            for item in self.inventory:
                if item_to_drop == item.name:
                    rooms[self.currentRoom]["items"].append(item)
                    print(item.name + " dropped.")
                    self.inventory.remove(item)
        else:
            print("Drop what, again?")

    def equip(self, item_to_equip):
        temp_item_list = []
        for item in self.inventory:
            temp_item_list.append(item.name)
        if item_to_equip in temp_item_list:
            for item in self.inventory:
                if item_to_equip == item.name and item.can_be_equipped is True:
                    item.is_equipped = True
                    print(item.name + " equipped.")

    def add_xp(self, xp):
        print(self.name + " had " + str(self.current_xp) + "xp.")
        self.current_xp += xp
        print(self.name + " now has " + str(self.current_xp) + " xp.")

    def level_up(self):
        xp_to_lvl_up = char_level_xp_req[self.rate][self.current_level + 1]
        if self.current_xp >= xp_to_lvl_up:
            print(self.name + " current level is: " + str(self.current_level))
            self.current_level += 1
            self.current_xp -= xp_to_lvl_up
            print(self.name + " current level is: " + str(self.current_level))
        else:
            print("Not enough XP to purchase the next level.")

#NOTE: NPCs are *NOT* monsters!
class NonPlayerCharacter(Character):
    """Common base class for all NPCs."""

    def __init__(self, name):
        self.name = name
        self.strength = 3
        self.vitality = 3
        self.hitPoints = int((self.vitality / 10) * random.randint(5, 30))
        self.attack = 1
        self.defense = 1
        self.inventory = []
        self.currentRoom = (0, 0)
        self.add_to_room()
        world_characters.append(self)
        self.equipment = []
        self.movement = 1
        self.direction = "north"

    def change_direction(self):
        directions = ["north", "south", "east", "west"]
        directions.remove(self.direction)
        self.direction = random.choice(directions)

    # def go(self, newroom):
    #     if move[1] in rooms[self.currentRoom]:
    #         rooms[self.currentRoom]["characters"].remove(self)
    #         self.currentRoom = rooms[self.currentRoom][move[1]]
    #         rooms[self.currentRoom]["characters"].append(self)
    #         self.view_surroundings()
    #     else:
    #         print("You can't go that way.")


"""
Notes on monsters:
Monsters will be randomly encountered - they do not "wander" the dungeon.
Monsters will not carry items, but will "drop" items at random.
Dropped items will be pulled from a pre-existing dictionary.
General monster parties will be procedurally built from pre-existing classes.
Dungeon level and average party member level will be considered in monster
party makeup.
"""

class Monster(object):
    def __init__(self, name, level):
        self.name = name
        self.baseHP = 1
        self.HP = self.baseHP * level
        self.baseAP = 1 #define a "base" attack power
        self.AP = self.baseAP * level

    def show_stats(self):
        print("Stats of monster '%s':" %self.name)
        print(vars(self))

class Item(object):
    def __init__(self):
        self.weight = 1
        self.description = ""
        self.general_name = ""
        self.description = "It's an item"
        self.name = "item"
        self.is_equipped = False
        self.can_be_equipped = False

class Weapon(Item):
    """All weapons can be described with this class."""

    def __init__(self, name, min_dmg, max_dmg, description):
        self.isweapon = True
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.can_be_equipped = True
        self.is_equipped = True
        self.description = description

# Procedural Methods

def showInstructions():
    """print a (temporary) "main menu", and the available commands"""
    print("WizardryClone")
    print("=============")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'drop [item]'")
    print("'inventory'")
    print("'status'")
    print("'look'")
    print("'attack'")

#In-town functions

def level_up(character):
    """Triggers the character's internal "level up" method."""
    player.level_up()

def party_add_character(character_type, n):
    """Creates a list of Character objects"""

# initialize mob and print its attributes
mob = Monster("orc", 1)
mob.show_stats()

# Item initialization - item names are case sensitive for now
sword1 = Weapon("sword", 1, 5, "This is a simple short sword of steel.")
item1 = Item()

# A single "dungeon" level
rooms = {
    (0, 0): {"name": "0,0",
             "description": "0,0",
             "east": (1, 0),
             "north": (0, 1),
             "items": [],
             "characters": []},
    (0, 1): {"name": "0,1",
             "description": "0,1",
             "south": (0, 0),
             "east": (1, 1),
             "items": [sword1, item1],
             "characters": []},
    (1, 0): {"name": "1,0",
             "description": "1,0",
             "north": (1, 1),
             "west": (0, 0),
             "items": [],
             "characters": []},
    (1, 1): {"name": "1,1",
             "description": "1,1",
             "south": (1, 0),
             "west": (0, 1),
             "items": [],
             "characters": []}
}

# A list of weapons
weapons = {
    "sword01": {"name": "Short Sword"}
}

# create characters, list of characters
player = Character()
goblin = NonPlayerCharacter("goblin")
orc = NonPlayerCharacter("orc")

# display "main menu"
showInstructions()

# loop
while True:

    move = input(">").lower().split()

    if move[0] == "go":
        player.go(move[1])
    elif move[0] == "get" or move[0] == "take":
        player.get(move[1])
    elif move[0] == "inventory":
        player.show_inventory()
    elif move[0] == "equip":
        player.equip(move[1])
    elif move[0] == "drop":
        player.drop(move[1])
    elif move[0] == "look":
        player.view_surroundings()
    elif move[0] == "list":
        for character in world_characters:
            print(character.name)
    elif move[0] == "placeme":
        player.place_random()
    elif move[0] == "place" and move[1] in rooms:
        player.place_room(move[1])
    elif move[0] == "attack":
        print("Not yet implemented.")
    elif move[0] == "look":
        player.view_surroundings()
    elif move[0] == "status":
        player.show_stats()
    elif move[0] == "addxp":
        player.add_xp(int(move[1]))
    elif move[0] == "levelup":
        player.level_up()
    else:
        print("I have no idea what you're trying to do.")

    if move[0] == "q" or move[0] == "quit":
        break

"""  This is just functionality for "wandering" NPCs.
    for character in world_characters:
        if isinstance(character, NonPlayerCharacter):
            print(character.name + " changes direction.")
            character.change_direction()
            print(character.name + " is now pointing %s" %character.direction)
            character.go(character.direction)
"""
