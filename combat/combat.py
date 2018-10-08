# Module for combat helper methods
from operator import attrgetter


def roll_for_initiative(player_party, mob_group):
    a = player_party
    b = mob_group
    for actor in a:
        actor.roll_init()
    for actor in b:
        actor.roll_init()


def build_combat_group(player_party, mob_group):
    """Build an entity for players and mobs.
    
    In the battle grid, the "row positions" are numerical keys so that the below
    routine(s) can iterate through them.
    0: left
    1: center
    2: right
    """
    battle_grid = {
            'mobs': {
                'front': {0: None, 1: None, 2: None},
                'back': {0: None, 1: None, 2: None},
                'reserve': {0: None, 1: None, 2: None}
                },
            'players': {
                'front': {0: None, 1: None, 2: None},
                'back': {0: None, 1: None, 2: None}
                }
            }
    
    player_stack = player_party
    mob_stack = mob_group

    # TODO: replace with a routine which uses pre-defined player group formation
    # to build player portion of the grid

    # Easier to type "mfr" than "battle_grid['mobs']['front'].values"
    mfr = battle_grid['mobs']['front'].values
    mbr = battle_grid['mobs']['back'].values
    mrr = battle_grid['mobs']['reserve'].values
    pfr = battle_grid['players']['front'].values
    pbr = battle_grid['players']['back'].values

    while len(mob_stack) > 0 and len(mfr) > 0:
        if len(mob_stack) > 0:
        for actor in mfr:
            actor = mob_stack.pop()
    while len(mob_stack) > 0 and len(mbr) > 0:
        for actor in mbr:
            actor = mob_stack.pop()
    while len(mob_stack) > 0 and len(mrr) > 0:
        for actor in mrr:
            actor = mob_stack.pop()
    while len(player_stack) > 0 and len(pfr) > 0:
        for actor in pfr:
            actor = 
            


    for actor in player_party:
        combatants.append(actor)
    for actor in mob_group:
        combatants.append(actor)
    combatants.sort(key=attrgetter('initiative'))

    return battle_grid


