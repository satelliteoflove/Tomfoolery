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
    """Build an entity for players and mobs."""
    battle_grid = {
            'mobs': {
                'front': {'left': None, 'center': None, 'right': None},
                'back': {'left': None, 'center': None, 'right': None},
                'reserve': {'left': None, 'center': None, 'right': None}
                },
            'players': {
                'front': {'left': None, 'center': None, 'right': None},
                'back': {'left': None, 'center': None, 'right': None}
                }
            }
    
    player_stack = player_party
    mob_stack = mob_group

    # TODO: replace with a routine which uses pre-defined player group formation
    # to build player portion of the grid

    for actor in battle_grid['mobs']['front'].values:
        if len(mob_stack) > 0:
            actor = mob_stack.pop()


    for actor in player_party:
        combatants.append(actor)
    for actor in mob_group:
        combatants.append(actor)
    combatants.sort(key=attrgetter('initiative'))

    return battle_grid


