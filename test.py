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

#Monsters
monster_catalog = {
    "goblin":{"typename":"goblin",
              "base_hp":5,
              "THAC0":1,
              "base_ap":1,
              "weapon":"claw",
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

world = World(WORLD_CONFIG)
