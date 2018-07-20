#Module for combat helper methods

def roll_for_initiative(player_party, mob_group):
    a = party
    b = mob_group
    for actor in a:
        actor.roll_init()
    for actor in b:
        actor.roll_init()

def build_combat_group(player_party, mob_group):
    player_party = player_party
    mob_group = mob_group

    #TODO: set combat_group to match what is currently in dm.py.
    combat_group = 0
