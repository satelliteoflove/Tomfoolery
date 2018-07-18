#Module for combat helper methods
from numpy import random
import collections

def roll_for_initiative(self, party, mob_group):
    a = party
    b = mob_group
    for actor in a:
        actor.roll_init()
    for actor in b:
        actor.roll_init()
