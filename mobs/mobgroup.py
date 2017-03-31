import mobs.mobs
from numpy import random

class MobGroup(object):
    """Class for storing monsters. For use during combat."""
    def __init__(self, max_party_weight, mob_list, count):
        self.members = []
        self.count = count
        self.remaining_weight = max_party_weight
        while self.remaining_weight > 0:
            #TODO: pull mob from level-specific list 
            newmob = mobs.mobs.Mob(
                mob_list,"goblin",random.randint(1,3)
            )
            if newmob.weight <= self.remaining_weight:
                self.remaining_weight -= newmob.weight
                self.members.append(newmob)

    def add_to_level(self, level):
        for member in self.members:
            level.mob_party.append(self)
