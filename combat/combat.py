#Module for combat helper methods
from numpy import random
import collections

def roll_for_initiative(self, party, mobgroup):
    for actor in party:
        actor.roll_init()
    for actor in mobgroup:
        actor.roll_init()
