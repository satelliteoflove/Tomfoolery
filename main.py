__author__ = 'Chris'


import random
import struct
import readline
import math
import numpy as np
import uuid

# World/Dungeon/Level configuration
worldCharacters = []
WORLD_CONFIG = {
    "dungeon_count": 1,
    "level_count":1,
    "level_width":4,
    "level_height":4
}

#This is the xp required to gain a level. It is the same for all classes, since
#different race/class combinations gain xp at different rates.
char_level_xp_req = {
    2:750,
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

char_class_traits = {
    "fighter":{"preferred_stat":"strength",
               "hp_bonus":5,
               "min_str":12,
               "min_agi":0,
               "min_int":0,
               "min_vit":0,
               "min_pie":0,
               "min_luk":0,
               "AC":1,
               "THAC0mult":1
              },
    "mage":{"preferred_stat":"intelligence",
            "hp_bonus":1,
            "min_str":0,
            "min_agi":0,
            "min_int":12,
            "min_vit":0,
            "min_pie":0,
            "min_luk":0,
            "AC":1,
            "THAC0mult":0.5
           },
    "priest":{"preferred_stat":"piety",
              "hp_bonus":3,
              "min_str":0,
              "min_agi":0,
              "min_int":0,
              "min_vit":0,
              "min_pie":12,
              "min_luk":0,
              "AC":1,
              "THAC0mult":.75
             }
}

print("Printing list of classes:")
for key in char_class_traits.keys():
    print(key)

# TODO: Add other races to list (following table in characters.md).

class World(object):
    dungeons = []
    def __init__(self, config):
        print("Generating the world...")
        self.dungeons = [
            Dungeon(config)
            for x in range(config["dungeon_count"])]
        print("Finished world generation.")

class Dungeon(object):
    levels = []
    def __init__(self, config):
        print("Beginning dungeon generation...")
        self.levels = [
            Level(config)
            for x in range(config["level_count"])]
        print("Finished dungeon generation.")

class Level(object):
    tiles = []
    def __init__(self, config):
        print("Beginning level generation...")
        for x in range(config["level_width"]):
            row = [Tile()
                   for y in range(config["level_height"])]
            self.tiles.append(row)
        mob_party = MonsterParty(1)
        print("Finished level generation.")

class Tile(object):
    def __init__(self):
        self.isExplored = False
        self.isPassable = True
        self.characters = []
        self.items = []

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
        target = worldCharacters[target]
        damage = damage
        status_effect = status
        target.HP += damage
        target.status_effect += status

class Weapon(Item):
    """All weapons can be described with this class."""

    def __init__(self, list_of_weapons, weapon_index):
        self.isweapon = True
        self.name = list_of_weapons[weapon_index]["name"]
        self.min_dmg = list_of_weapons[weapon_index]["min_dmg"]
        self.max_dmg = list_of_weapons[weapon_index]["max_dmg"]
        self.can_be_equipped = True
        self.is_equipped = False
        self.description = list_of_weapons[weapon_index]["description"]

WEAPON_BASE_TYPES = {
    1:{
        "name":"claw",
        "min_dmg":1,
        "max_dmg":5,
        "description":"Natural claws."
    }
}

class Character(object):
    """Common base class for all PCs and NPCs."""

    def __init__(self):
        self.name = self.set_name()
        self.uuid = uuid.uuid4()
        self.currentLevel = 1
        self.currentXP = 0
        self.set_race()
        self.set_sex()
        self.set_bonusPoints()
        self.set_class()
        self.statNames = ["strength", "agility", "vitality", "intelligence",
                           "piety", "luck"]
        self.assign_BonusPoints()
        self.set_xp_rate()
        self.set_initial_HP()
        self.set_class_AC() #As in characters.md - AD&D rules for AC/THAC0.
        self.set_THAC0()
        self.inventory = []
        self.currentRoom = (0, 0)
        self.add_to_room()
        self.direction = "north"
        worldCharacters.append(self)
        self.equipment = []
        self.set_AP()

    def set_class_AC(self):
        """Set character's class-based AC "base"."""
        self.AC = char_class_traits[self.char_class]["AC"]

    def set_THAC0(self):
        """Set character's class-based THAC0 "base"."""
        self.THAC0 = 20 - round((self.currentLevel *
                           char_class_traits[self.char_class]["THAC0mult"]))

    def set_initial_HP(self):
        """Used to set *initial* HP for character.

        Depending on the character's class, a different amount of starting HP
        may be generated. A minimum of 2HP will be assigned to any starting
        character.

        TODO: Adjust vitality modifier for HP. There should be a "curve", where
        characters with especially low vitality get a penalty and high vitality
        grants a bonus, but this should be mild (not a multiplier based on
        vitality?).
        """
        self.hitPoints = 0
        self.maxHitPoints = 0
        chance = random.randint(0,1)

        if self.char_class == "samurai":
            if chance == 0:
                self.hitPoints = int(16 + self.vitality // 2)
            if chance == 1:
                self.hitPoints = (9 * (16 + self.vitality // 2) // 10)
        elif self.char_class == "fighter" or self.char_class == "lord":
            if chance == 0:
                self.hitPoints = 10 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (10 + self.vitality // 2) // 10)
        elif self.char_class == "priest":
            if chance == 0:
                self.hitPoints = 8 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (8 + self.vitality // 2) // 10)
        elif self.char_class == "thief" or self.char_class == "ninja":
            if chance == 0:
                self.hitPoints = 6 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self.vitality // 2) // 10)
        elif self.char_class == "bishop":
            if chance == 0:
                self.hitPoints = 6 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self.vitality // 2) // 10)
        elif self.char_class == "mage":
            if chance == 0:
                self.hitPoints = 4 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (4 + self.vitality // 2) // 10)

        if self.hitPoints < 2:
            self.hitPoints = 2

        self.maxHitPoints = self.hitPoints

    def add_maxHP(self):
        """Adds max HP when character gains a level.

        TODO: Ensure that vitality modifies added maximum HP.
        """
        if self.char_class == "fighter" or self.char_class == "lord":
            self.maxHitPoints += int(random.triangular(0,10,5))
        elif self.char_class == "priest" or self.char_class == "samurai":
            self.maxHitPoints += int(random.triangular(0,8,4))
        elif self.char_class == "monk":
            self.maxHitPoints += int(random.triangular(0,8,5))
        elif self.char_class == "thief" or self.char_class == "ninja":
            self.maxHitPoints += int(random.triangular(0,6,3))
        elif self.char_class == "bishop":
            self.maxHitPoints += int(random.triangular(0,6,3))
        elif self.char_class == "mage":
            self.maxHitPoints += int(random.triangular(0,4,2))

    def set_sex(self):
        """Sets the sex of the character.

        The sex of a character grants a one-time stat bonus upon character
        creation (+1 VIT (F)/+1 STR (M)), and only women can be valkyries.
        """
        self.sex = ""
        while self.sex != "male" and self.sex != "female":
            print("What is the sex of the character?\n(male or female)")
            self.sex = input().lower()
        if self.sex == "male":
            self.strength += 1
        elif self.sex == "female":
            self.vitality += 1

    def set_bonusPoints(self):
        """Assigns starting bonus points.
        """
        self.bonusPoints = 0
        while self.bonusPoints < 4:
            self.bonusPoints = int(np.random.normal(8, 4))
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
        total bonus points required vs current bonus points.
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

    def assign_BonusPoints(self):
        print("There are " + str(self.bonusPoints) + " remaining BP.")
        print("Your current statistics are: ")
        print("[S]trength: " + str(self.strength))
        print("[A]gility: " + str(self.agility))
        print("[V]itality: " + str(self.vitality))
        print("[I]ntelligence: " + str(self.intelligence))
        print("[P]iety: " + str(self.piety))
        print("[L]uck: " + str(self.luck))
        while self.bonusPoints > 0:
            stat_increased = 's'
#            stat_increased = input().lower()
            if stat_increased == 's':
                stat_increased = "strength"
            elif stat_increased == 'a':
                stat_increased = "agility"
            elif stat_increased == 'v':
                stat_increased = "vitality"
            elif stat_increased == 'i':
                stat_increased = "intelligence"
            elif stat_increased == 'p':
                stat_increased = "piety"
            elif stat_increased == 'l':
                stat_increased = "luck"

            if stat_increased not in self.statNames:
                print("That isn't a stat. Try again.")
            else:
                setattr(self, stat_increased, getattr(self, stat_increased) + 1)
                self.bonusPoints -= 1
                print("Bonus Points = " + str(self.bonusPoints))
                print("Strength: " + str(self.strength))
                print("Agility: " + str(self.agility))
                print("Vitality: " + str(self.vitality))
                print("Intelligence: " + str(self.intelligence))
                print("Piety: " + str(self.piety))
                print("Luck: " + str(self.luck))
        print("You don't have any bonus points left.")

    def set_xp_rate(self):
        """Sets the experience multiplier for a given race/class combination.
        """
        print("Setting xp rate multiplier.")
        print("self.char_class = " + self.char_class)
        print("self.race = " + self.race)
        print("My 'rate' is: " + str(
                            char_race_xp_rate[self.race][self.char_class]))
        if self.race in char_race_xp_rate:
            if self.char_class in char_race_xp_rate[self.race]:
                self.rate = char_race_xp_rate[self.race][self.char_class]
            else:
                print("That class doesn't exist for that race.")
        else:
            print("That race isn't in the list of xp rates.")

    def set_AP(self):
        """AP is a function of strength, which may change upon gaining a level.

        AP is a basic per-hit damage modifier.  Characters with very low
        strength have a damage penalty, whereas characters with very high
        strength have a damage bonus.
        """
        self.AP = 0
        if self.strength == 3:
            self.AP -= 3
        if self.strength == 4:
            self.AP -= 2
        if self.strength == 5:
            self.AP -= 1
        if self.strength > 15:
            self.AP += 1 * (self.strength - 15)
        if self.AP < 0:
            self.AP = 0
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
        #self.view_surroundings()

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
        print("Nearby, you see " +
              str(len(current_room_character_list)) + " characters:")
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
            #self.view_surroundings()
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
        #Generates a series of 28 multipliers to be used when calculating xp
        #gained.
        xp_multipliers = np.linspace(1.0,0.5,num=28)
        print(self.name + " had " + str(self.currentXP) + "xp.")
        x = char_race_xp_rate[self.race][self.char_class]
        print("Your xp multiplier is: " + str(xp_multipliers[x - 1]))
        self.currentXP += int((xp * xp_multipliers[x - 1]))
        print(self.name + " now has " + str(self.currentXP) + " xp.")

    def level_up(self):
        xp_to_lvl_up = char_level_xp_req[self.currentLevel + 1]
        if self.currentXP >= xp_to_lvl_up:
            print(self.name + " current level is: " + str(self.currentLevel))
            self.currentLevel += 1
            self.currentXP -= xp_to_lvl_up
            self.add_maxHP()
            print(self.name + " current level is: " + str(self.currentLevel))
        else:
            print("Not enough XP to purchase the next level.")

    def take_dmg(self, dmg):
        self.hitPoints -= dmg
        if self.hitPoints <= 0:
            print(self.name + "is dead.")

    def attack(self, target):
        dmg = self.AP + 1
        target.take_dmg(dmg)
        print("I am attacking " + target.name + " for " + str(dmg) +
              " points of damage.")

class Party(object):
    """Class for storing characters in a group.
    """
    def __init__(self):
        self.xy_pos = (0,0)
        self.currentRoom = []
        self.members = {}
        self.encounter_chance = 0.0

    def add_char(self, character):
        print("Current members:")
        list(self.members)
        self.members[character.uuid] = character
        list(self.members)

    def move(self, direction):
        print("moving party..." + direction)
        for member in self.members.values():
            print("value of member uuid: " + str(member.uuid))
            print("member name: " + member.name)
            member.go(direction)
        next(iter(self.members.values())).view_surroundings()

    def rem_char(self, character):
        print("Current members:")
        list(self.members)
        self.members[character.uuid].remove()
        list(self.members)


#Monsters
monster_catalog = {
    "goblin":{"typename":"goblin",
              "base_hp":5,
              "THAC0":1,
              "base_ap":1,
              "weapon":Weapon(WEAPON_BASE_TYPES,1),
              "party_weight":1
             }
}

class Monster(object):
    def __init__(self, config, type_name, level):
        self.type_name = config[type_name]["typename"]
        self.name = self.type_name
        self.HP = config[type_name]["base_hp"] * level
        self.THAC0 = monster_catalog[type_name]["THAC0"]
        self.AP = monster_catalog[type_name]["base_ap"] * level // 2
        self.weapon = config[type_name]["weapon"]
        self.weight = config[type_name]["party_weight"]
        worldCharacters.append(self)
        if self.AP < 1:
            self.AP = 1

    def attack(self, target):
        dmg = self.AP + 1
        target.take_dmg(dmg)
        print("I am attacking " + target.name + " for " + str(dmg) +
              " points of damage.")

    def take_dmg(self, dmg):
        self.hitPoints -= dmg
        if self.hitPoints <= 0:
            print(self.name + "is dead.")

    def show_stats(self):
        print("Stats of monster '%s':" %self.name)
        print(vars(self))

class MonsterParty(Party):
    """Class for storing monsters. For use during combat."""
    def __init__(self, party_weight):
        self.members = []
        self.remaining_weight = party_weight
        while self.remaining_weight > 0:
            monster = Monster(
                monster_catalog,"goblin",random.randint(1,3)
            )
            if monster.weight <= self.remaining_weight:
                self.remaining_weight -= monster.weight
                self.members.append(monster)

#Items
class ItemMaker(object):
    def __init__(self):
        self.weight = 1
        self.description = ""
        self.general_name = ""
        self.description = "It's an item"
        self.name = "item"
        self.is_equipped = False
        self.can_be_equipped = False



# Begin initialization and presentation.

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

# World initialization
# world = World() # - broken for now (until variable/parameter work is finished)

# Item initialization - item names are case sensitive for now
claws2 = Weapon(WEAPON_BASE_TYPES,1)
item1 = Item()

# Four rooms for testing other functions.
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
             "items": [claws2, item1],
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

# create characters, list of characters
player = Character()
#player2 = Character()
party1 = Party()
party1.add_char(player)

print("The following characters are in the world list:")
for character in worldCharacters:
    print(character.name)

# display "main menu"
showInstructions()

# loop
while True:

    move = input(">").lower().split()

    if move[0] == "go":
        party1.move(move[1])
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
        for character in worldCharacters:
            print(character.name)
    elif move[0] == "placeme":
        player.place_random()
    #elif move[1] == "place" and move[1] in rooms:
    #    player.place_room(move[1])
    elif move[0] == "attack" and move[1]:
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
#    elif move[0] == "abp":
#        player.assign_BonusPoints()
    elif move[0] == "q" or move[0] == "quit":
        break
    else:
        print("I have no idea what you're trying to do.")
