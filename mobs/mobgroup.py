from . import mobs
from numpy import random

class MobGroup(object):
    """Class for storing monsters. For use during combat."""
    def __init__(self, mob_list, max_weight):
        self.members = []
        self.remaining_weight = max_weight
        self.mob_list = mob_list
        self.members.append(mobs.Mob(self.mob_list, "goblin", 1))

    def add_to_level(self, level):
        for member in self.members:
            level.mob_party.append(self)
