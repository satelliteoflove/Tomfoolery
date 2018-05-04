from . import mobs
from numpy import random

class MobGroup(object):
    """Class for storing monsters. For use during combat."""
    def __init__(self, mob_list, max_weight):
        self.members = []
        self.remaining_weight = max_weight
        self.mob_list = mob_list
        while self.remaining_weight > 0:
            newmob = mobs.Mob(self.mob_list,"goblin",1)
            self.members.append(newmob)
            self.remaining_weight -= newmob.weight
            print(newmob.name + " appears!")

    def list_members(self):
        for member in self.members:
            print(member.name)
