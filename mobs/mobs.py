import characters
from numpy import random
import collections
import items

class Mob(object):
    def __init__(self, mob_list, type_name, level):
        self.type_name = mob_list[type_name]["typename"]
        self.name = self.type_name
        self.HP = mob_list[type_name]["base_hp"] * level
        self.THAC0 = mob_list[type_name]["THAC0"]
        self.AP = mob_list[type_name]["base_ap"] * level // 2
        #self.weapon = mob_list[type_name]["weapon"]
        self.weight = mob_list[type_name]["party_weight"]
        if self.AP < 1:
            self.AP = 1

    def attack(self, target):
        dmg = self.AP + 1
        target.take_dmg(dmg)

    def take_dmg(self, dmg):
        self.hitPoints -= dmg
        if self.hitPoints <= 0:
            print(self.name + "is dead.")

    def show_stats(self):
        print("Stats of monster '%s':" %self.name)
        print(vars(self))

