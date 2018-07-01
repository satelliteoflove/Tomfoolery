from . import mobs
from numpy import random

class MobGroup(object):
    """Class for storing monsters. For use during combat."""
    def __init__(self, mob_list, max_weight):
        self.members = []
        self.remaining_weight = max_weight
        self.mob_list = mob_list
        while self.remaining_weight > 0:
            newmob = mobs.Mob(self.mob_list,"ant",random.randint(1,3))
            self.members.append(newmob)
            self.remaining_weight -= newmob.weight

    def list_members(self):
        for member in self.members:
            print("a level " + str(member.level) + " " + member.name +
                 " appears!")

    def check_friendly(self):
        chance = 0
        for mob in self.members:
            if mob.alignment == "evil":
                chance += 0
            elif mob.alignment == "neutral":
                chance += 50
            elif mob.alignment == "good":
                chance += 100
        if chance > 0:
            chance = chance / len(self.members)
        a = random.randint(1,99)
        print(str(chance) + "% friendly vs roll of " + str(a) + ".")
        if chance > a:
            return True
        else:
            return False
