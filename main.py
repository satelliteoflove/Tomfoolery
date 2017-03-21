__author__ = 'Chris'


import struct
import readline
from numpy import random
import collections
from characters.pc import Character
from world import World
from world import Dungeon
from world import Level
from world import Tile

worldCharacters = []

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

    def monster_encounter(self, party_weight, level):
        print("Encounter!")
        monster_party = MonsterParty(party_weight)
        print("You have encountered: ")
        for monster in monster_party.members:
            print(monster.name)

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

    def add_to_level(self, level):
        for member in self.members:
            level.mob_party.append(self)

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

mobparty = MonsterParty(1)

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
    elif move[0] == "encounter":
        party1.monster_encounter(1,0)
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
