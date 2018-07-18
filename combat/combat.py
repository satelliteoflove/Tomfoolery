#Module for combat helper methods

def roll_for_initiative(self, party, mob_group):
    a = party
    b = mob_group
    for actor in a:
        actor.roll_init()
    for actor in b:
        actor.roll_init()
