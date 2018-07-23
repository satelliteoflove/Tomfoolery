#Module for combat helper methods
from operator import attrgetter

def roll_for_initiative(player_party, mob_group):
    a = player_party
    b = mob_group
    for actor in a:
        actor.roll_init()
    for actor in b:
        actor.roll_init()

def build_combat_group(player_party, mob_group):
    """Build an entity for players and mobs."""
    battle_grid = {
            'mobs': {
                'front': {},
                'back': {}
                },
            'players': {
                'front': {},
                'back': {}
                }
            }
    
    player_party = player_party
    mob_group = mob_group

    #TODO: combatants will be replace by battle_grid
    combatants = []
    for actor in player_party:
        combatants.append(actor)
    for actor in mob_group:
        combatants.append(actor)
    combatants.sort(key = attrgetter('initiative'))

    return combatants
