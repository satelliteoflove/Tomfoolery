from . import mobs
from numpy import random

class MobGroup(object):
    """Class for storing monsters. For use during combat."""
    def __init__(self):
        self.members = []
        #while self.remaining_weight > 0:
        #    #TODO: pull mob from level-specific list 
        #    newmob = mobs.mobs.Mob(
        #        mob_list,"goblin",random.randint(1,3)
        #    )
        #    if newmob.weight <= self.remaining_weight:
        #        self.remaining_weight -= newmob.weight
        #        self.members.append(newmob)
    def set_remaining_weight(self, weight):
        self.remaining_weight = weight

    def add_mob(self, mob):
        """Adds given mob to group.

        Parameters
        ----------
        mob : object
           Approved mob being passed to the group.
        """
        self.members.append(mob)

    def add_to_level(self, level):
        for member in self.members:
            level.mob_party.append(self)
