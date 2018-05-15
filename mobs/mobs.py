import characters
from numpy import random
import collections
import items

class Mob(object):
    def __init__(self, mob_list, type_name, level):
        self.type_name = mob_list[type_name]["typename"]
        self.type = mob_list[type_name]["type"]
        self.name = self.type_name
        self.level = level
        self.agility = mob_list[type_name]["agility"]
        self.HP = mob_list[type_name]["base_hp"] * self.level
        self.THAC0 = mob_list[type_name]["THAC0"]
        self.AP = mob_list[type_name]["base_ap"] * self.level // 2
        self.weight = round(mob_list[type_name]["party_weight"] * self.level, 1)
        self.weapon_slots = mob_list[type_name]["wslots"]
        self.attacks = mob_list[type_name]["attacks"]
        self.alignment = mob_list[type_name]["alignment"]
        if self.AP < 1:
            self.AP = 1

    def roll_init(self):
        self.initiative = random.randint(1,100)

    def attack(self, target):
        dmg = self.AP + 1
        target.take_dmg(dmg)

    def show_stats(self):
        print("Stats of monster '%s':" %self.name)
        print(vars(self))

