__author__ = 'Chris'


import random
import struct
import readline
import math

# Globals
world_characters = []
MAP_WIDTH = 0
MAP_HEIGHT = 0

# Character levels (universal)
# Note that experience required to gain a level are based on a combination of
# character class and character race. All races gain levels in different classes
# at different rates. 28 different rates are applied, with the lowest
# requirement at rate 1 and the highest requirement at 28.


EFFECTS = {"heal1":1}

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

char_race_traits = {
    "human":{"min_str":9,
             "max_str":19,
             "min_int":8,
             "max_int":18,
             "min_pie":8,
             "max_pie":18,
             "min_vit":9,
             "max_vit":19,
             "min_agi":8,
             "max_agi":18,
             "min_luk":8,
             "max_luk":18
            },
    "elf":{"min_str":7,
           "max_str":17,
           "min_int":10,
           "max_int":20,
           "min_pie":10,
           "max_pie":20,
           "min_vit":7,
           "max_vit":17,
           "min_agi":9,
           "max_agi":19,
           "min_luk":8,
           "max_luk":18
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
             "ninja":28
            },
    "elf":{"fighter":6,
           "mage":3,
           "priest":3,
           "thief":6,
           "alchemist":9,
           "bishop":11,
           "bard":5,
           "ranger":8,
           "psionic":16,
           "valkyrie":11,
           "samurai":14,
           "lord":23,
           "monk":15,
           "ninja":27
          }
}

# TODO: Make sure that all dictionary value sets contain all variables.
char_class_traits = {
    "fighter":{"preferred_stat":"strength",
               "hp_bonus":5,
               "min_str":12,
               "min_agi":0,
               "min_int":0,
               "min_vit":0,
               "min_pie":0,
               "min_luk":0
              },
    "mage":{"preferred_stat":"intelligence",
            "hp_bonus":1,
            "min_str":0,
            "min_agi":0,
            "min_int":12,
            "min_vit":0,
            "min_pie":0,
            "min_luk":0
           },
    "priest":{"preferred_stat":"piety",
              "hp_bonus":3,
              "min_str":0,
              "min_agi":0,
              "min_int":0,
              "min_vit":0,
              "min_pie":12,
              "min_luk":0
             }
}


print("Printing list of classes:")
for key in char_class_traits.keys():
    print(key)

# TODO: Add other races to list following table in characters.md.


class Character(object):
    """Common base class for all PCs and NPCs."""

    def __init__(self):
        self.name = self.set_name()
        self.current_level = 1
        self.current_xp = 0
        self.set_race()
        self.set_sex()
        self.set_bonusPoints()
        self.set_class()
        self.set_xp_rate()
        self.set_HP()
        self.AP = self.current_level
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

    def set_HP(self):
        """Used to set *initial* HP for character.

        Depending on the character's class, a different amount of starting HP
        may be generated. A minimum of 2HP will be assigned to any starting
        character.

        TODO: Adjust vitality modifier for HP.
        """
        self.hitPoints = 0
        self.max_hitPoints = 0
        chance = random.randint(0,1)
        if self.char_class == "samurai":
            if chance == 0:
                self.hitPoints = int(16 + self.vitality // 2)
            if chance == 1:
                self.hitPoints = (9 * (16 + self.vitality // 2) // 10)
        if self.char_class == "fighter" or self.char_class == "lord":
            if chance == 0:
                self.hitPoints = 10 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (10 + self.vitality // 2) // 10)
        if self.char_class == "priest":
            if chance == 0:
                self.hitPoints = 8 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (8 + self.vitality // 2) // 10)
        if self.char_class == "thief" or self.char_class == "ninja":
            if chance == 0:
                self.hitPoints = 6 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self.vitality // 2) // 10)
        if self.char_class == "bishop":
            if chance == 0:
                self.hitPoints = 6 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self.vitality // 2) // 10)
        if self.char_class == "mage":
            if chance == 0:
                self.hitPoints = 4 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (4 + self.vitality // 2) // 10)
        if self.hitPoints < 2:
            self.hitPoints = 2
        self.max_hitPoints = self.hitPoints

    def add_maxHP(self):
        """Adds max HP when character gains a level.
        """
        if self.char_class == "fighter" or self.char_class == "lord":
            self.max_hitPoints += int(random.triangular(0,10,5))
        if self.char_class == "priest" or self.char_class == "samurai":
            self.max_hitPoints += int(random.triangular(0,8,4))

    def set_sex(self):
        self.sex = ""
        while self.sex != "male" and self.sex != "female":
            print("What is the sex of the character?\n(male or female)")
            self.sex = input().lower()
        if self.sex == "male":
            self.strength += 1
        elif self.sex == "female":
            self.vitality += 1

    def set_bonusPoints(self):
        self.bonusPoints = 0
        while self.bonusPoints < 4:
            self.bonusPoints = math.floor(random.triangular(1,25,5))
        print("Bonus Points = " + str(self.bonusPoints))
    def set_race(self):
        """Used on character creation to set race values.

        After choosing a race, the minimum stat values are set for the character
        based on racial minimums.  In addition, any special fields such as
        resistance values or special attacks are set.
        """
        print("What race is this character?\nChoose from the following:")
        for key in char_race_traits.keys():
            print(key)
        self.race = ""
        while self.race == "":
            tryrace = input().lower()
            if tryrace in char_race_traits:
                self.race = tryrace
            else:
                print("That is not a valid race.")
                print("What race is this character?\nChoose from the following:")
                for key in char_race_traits.keys():
                    print(key)
        self.strength = char_race_traits[self.race]["min_str"]
        self.vitality = char_race_traits[self.race]["min_vit"]
        self.agility = char_race_traits[self.race]["min_agi"]
        self.intelligence = char_race_traits[self.race]["min_int"]
        self.piety = char_race_traits[self.race]["min_pie"]
        self.luck = char_race_traits[self.race]["min_luk"]

    def set_name(self):
        name_accepted = False
        while name_accepted == False:
            try_name = input("What is the player's name?\n")
            if len(try_name) > 12:
                print("Name is too long. Must be 12 characters or less.")
            else:
                name_accepted = True
        return try_name

    def validate_class(self, newclass):
        """Validates that a class can be chosen for the character by comparing
        total bonus opints required vs current bonus points.
        """
        points_required = 0
        str_req = char_class_traits[newclass]["min_str"]
        agi_req = char_class_traits[newclass]["min_agi"]
        vit_req = char_class_traits[newclass]["min_vit"]
        int_req = char_class_traits[newclass]["min_int"]
        pie_req = char_class_traits[newclass]["min_pie"]
        luk_req = char_class_traits[newclass]["min_luk"]

        if str_req > self.strength:
            points_required += str_req - self.strength
        if agi_req > self.agility:
            points_required += agi_req - self.agility
        if vit_req > self.vitality:
            points_required += vit_req - self.vitality
        if pie_req > self.piety:
            points_required += pie_req - self.piety
        if luk_req > self.luck:
            points_required += luk_req - self.luck

        #sums all "min_stat"-type key values
        #for key, value in char_class_traits[newclass].items():
        #    if key.startswith('min_'):
        #        
        #        points_required += value
        #        print(str(points_required))
        if points_required > self.bonusPoints:
            return False
        else:
            return True

    def set_class(self):
        """Modifications specific to class changes.

        Includes statistic changes, class variable update, etc.
        In addition, the rate of HP growth is defined here.
        """
        classlist = []
        for classname in char_class_traits.keys():
            if self.validate_class(classname):
                print(classname)
                classlist.append(classname)
        print("The following classes are available: ")
        print(classlist)
        try_class = input().lower()
        satisfied = False
        while satisfied == False:
            if try_class not in classlist:
                print("That class isn't in the list. Try again.")
                try_class = input().lower()
            else:
                self.char_class = try_class
                satisfied = True
                str_req = char_class_traits[try_class]["min_str"]
                agi_req = char_class_traits[try_class]["min_agi"]
                vit_req = char_class_traits[try_class]["min_vit"]
                int_req = char_class_traits[try_class]["min_int"]
                pie_req = char_class_traits[try_class]["min_pie"]
                luk_req = char_class_traits[try_class]["min_luk"]

                if str_req > self.strength:
                    self.bonusPoints -= str_req - self.strength
                    self.strength = str_req
                if agi_req > self.agility:
                    self.bonusPoints -= agi_req - self.agility
                    self.agility = agi_req
                if vit_req > self.vitality:
                    self.bonusPoints -= vit_req - self.vitality
                    self.vitality = vit_req
                if pie_req > self.piety:
                    self.bonusPoints -= pie_req - self.piety
                    self.piety = pie_req
                if luk_req > self.luck:
                    self.bonusPoints -= luk_req - self.luck
                    self.luck = luk_req

    def assign_BP(self):
        if self.bonusPoints <= 0:
            print("You don't have any bonus points left.")
        else:
            print("There are " + str(self.bonusPoints) + " remaining BP.")
            print("Your current statistics are: ")
            print("Strength: " + str(self.strength))
            print("Agility: " + str(self.agility))
            print("Vitality: " + str(self.vitality))
            print("Intelligence: " + str(self.intelligence))
            print("Piety: " + str(self.piety))
            print("Luck: " + str(self.luck))
            while self.bonusPoints > 0:
                stat_increased = input().lower()
                

    def set_xp_rate(self):
        print("self.char_class = " + self.char_class)
        print("self.race = " + self.race)
        if self.race in char_race_xp_rate:
            if self.char_class in char_race_xp_rate[self.race]:
                self.rate = char_race_xp_rate[self.race][self.char_class]
            else:
                print("That class doesn't exist for that race.")
        else:
            print("That race isn't in the list of xp rates.")

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

class ItemMaker(object):
    def __init__(self):
        self.weight = 1
        self.description = ""
        self.general_name = ""
        self.description = "It's an item"
        self.name = "item"
        self.is_equipped = False
        self.can_be_equipped = False

    ITEM_TYPES = {
        "potion":{
            "equippable":False,
            "total_wearable":0,
            "usable":True,
            "break_chance":1.0,
            "clean_on_break":True,
            "effect1":"heal1",
            "effect2":"",
            "effect3":"",
            "targets":("self","party")
        }
    }

    ITEM_AFFIXES = {"healing":{1:"heal1"}}

    ITEM_SUFFIXES = {"silver":{1:"silver"}}


class Item(object):
    def __init__(self):
        self.weight = 1
        self.description = ""
        self.general_name = ""
        self.description = "It's an item"
        self.name = "item"
        self.is_equipped = False
        self.can_be_equipped = False

    def effect(self,target,damage,status):
        target = world_characters[target]
        damage = damage
        status_effect = status
        target.HP += damage
        target.status_effect += status

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
    elif move[0] == "bonuspoints":
        player.bonusPoints = int(move[1])
    elif move[0] == "classchange":
        player.set_class()
    elif move[0] == "q" or move[0] == "quit":
        break
    else:
        print("I have no idea what you're trying to do.")


"""  This is just functionality for "wandering" NPCs.
    for character in world_characters:
        if isinstance(character, NonPlayerCharacter):
            print(character.name + " changes direction.")
            character.change_direction()
            print(character.name + " is now pointing %s" %character.direction)
            character.go(character.direction)
"""
