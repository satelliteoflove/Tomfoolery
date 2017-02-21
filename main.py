__author__ = 'Chris'

import random
import struct
import readline

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

char_race_xp_rate = {
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

char_class_traits = {
    "fighter":{"preferred_stat":"strength",
               "hp_bonus":5,
               "min_str":10
              },
    "mage":{"preferred_stat":"intelligence",
            "hp_bonus":1,
            "min_int":10
           }
}

print("Printing list of classes:")
for key in char_class_traits.keys():
    print(key)

# TODO: Add other races to list following table in characters.md.


class Character(object):
    """Common base class for all PCs and NPCs."""

    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.current_level = 1
        self.current_xp = 0
        self.rate = 1
        self.char_class = "fighter"
        self.sex = "male"
        self.strength = 8
        self.vitality = 8
        self.hitPoints = int((self.vitality / 10) * random.randint(5, 30))
        self.AP = self.current_level
        self.bonusPoints = random.randint(5, 25)
        self.defense = 1
        self.inventory = []
        self.currentRoom = (0, 0)
        self.add_to_room()
        self.direction = "north"
        world_characters.append(self)
        self.equipment = []

        self.update_AP()

        if self.AP < 1:
            self.AP = 1

    def set_race(self):
        print("What race is this character?\nChoose from the following:")
        for key in char_race_xp_rate.keys():
            print(key)
        self.race = input().lower()

    def set_name(self):
        try_name = input("What is the player's name?\n")
        if len(try_name) > 12:
            print("Name is too long. Must be 12 characters or less.")
        else:
            self.name = try_name

    def class_change(self, new_class):
        """Modifications specific to class changes.

        Includes statistic changes, class variable update, etc.

        Keyword arguments:
        new_class -- class the character is changing to.
        """
        if "min_str" in char_class_traits[self.char_class]:
            min_str = char_class_traits[self.char_class]["min_str"]
        if "min_agi" in char_class_traits[self.char_class]:
            min_agi = char_class_traits[self.char_class]["min_agi"]
        if "min_vit" in char_class_traits[self.char_class]:
            min_vit = char_class_traits[self.char_class]["min_vit"]
        if "min_int" in char_class_traits[self.char_class]:
            min_int = char_class_traits[self.char_class]["min_int"]
        if "min_wis" in char_class_traits[self.char_class]:
            min_wis = char_class_traits[self.char_class]["min_wis"]
        if "min_cha" in char_class_traits[self.char_class]:
            min_cha = char_class_traits[self.char_class]["min_cha"]

        self.char_class = new_class

    def update_AP(self):
        """Updates stats which may change during play outside of lvl_up.

        This method is ONLY for calculating updated AP for the character. This
        method incorporates player level, class, appropriate class stat
        (strength for fighters, agility for thieves, etc.), equipment modifiers
        and status effects.
        """
        # Pull value of class-specific "preferred stat".
        stat = getattr(self,
                      char_class_traits[self.char_class]["preferred_stat"])

        print("This character's main stat is: " +
              char_class_traits[self.char_class]["preferred_stat"])
        self.AP = self.current_level + stat
        print("This character's AP is: " + str(self.AP))

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
        rooms[self.currentRoom]["characters"].remove(self)
        self.currentRoom = random.randrange(1,len(rooms))
        rooms[self.currentRoom]["characters"].append(self)
        self.view_surroundings()

# This code isn't right. Fix "go" code first.
#    def place_room(self, room: int):
#        if room > 0 and room <= len(rooms):
#            rooms[self.currentRoom]["characters"].remove(self)
#            self.currentRoom = rooms[self.currentRoom][
#        self.add_to_room()

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
        if newroom in rooms[self.currentRoom]:
            rooms[self.currentRoom]["characters"].remove(self)
            self.currentRoom = rooms[self.currentRoom][newroom]
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

    def attack(self, target):
        count = 0
        for character in world_characters:
            if character.name == target:
                count += 1
                dmg = self.AP
                print("I am attacking " + character.name + " for " + str(dmg) +
                      " points of damage.")
                break
        if count == 0:
            print("That didn't work.")

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

monster_catalog = {
    "goblin":{"typename":"goblin",
              "base_hp":5,
              "base_ap":1
             }
}

class Monster(object):
    def __init__(self, type_name, level):
        self.type_name = monster_catalog[type_name]["typename"]
        self.name = type_name + str(len(world_characters))
        self.HP = monster_catalog[type_name]["base_hp"] * level // 2
        self.baseAP = monster_catalog[type_name]["base_ap"]
        if self.baseAP > 1:
            self.AP = monster_catalog[type_name]["base_ap"] * level // 2
        else:
            self.AP = 1
        world_characters.append(self)

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

def party_add_character(character_type, n):
    """Creates a list of Character objects"""


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
# initialize mob and print its attributes
mob1 = Monster("goblin", 1)
mob2 = Monster("goblin", 2)


print("The following characters are in the world list:")
for character in world_characters:
    print(character.name)

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
        player.attack(move[1])
    elif move[0] == "look":
        player.view_surroundings()
    elif move[0] == "status":
        player.show_stats()
    elif move[0] == "addxp":
        player.add_xp(int(move[1]))
    elif move[0] == "levelup":
        player.level_up()
    elif move[0] == "help":
        showInstructions()
        dir(player)
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
