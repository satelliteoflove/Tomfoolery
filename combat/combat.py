# Module for combat helper methods
# Imports


def roll_for_initiative(player_party, mob_group):
    a = player_party
    b = mob_group
    for actor in a:
        actor.roll_init()
    for actor in b:
        actor.roll_init()


def set_formation(party):
    """For given party, set battle position of each actor.

    :party: TODO
    :returns: TODO

    """
    pass


def get_formation(party):
    """For given party, return battle position of each actor.

    :party: TODO
    :returns: TODO

    """
    pass


def build_combat_group(player_party, mob_group):
    """Build an entity for players and mobs. Expects lists of tuples, with
    actor/location values.
    """
    
    player_stack = player_party
    mob_stack = mob_group

    battle_grid = {
            'mfr': {'left': None, 'center': None, 'right': None},
            'mbr': {'left': None, 'center': None, 'right': None},
            'mrr': {'left': None, 'center': None, 'right': None},
            'pfr': {'left': None, 'center': None, 'right': None},
            'pbr': {'left': None, 'center': None, 'right': None}
            }

    # TODO: replace with a routine which uses pre-defined player group formation
    # to build player portion of the grid

    for location in battle_grid['mfr'].keys():
        if len(mob_stack) > 0:
            location = mob_stack.pop()
    for location in battle_grid['mbr'].keys():
        if len(mob_stack) > 0:
            location = mob_stack.pop()
    for location in battle_grid['mrr'].keys():
        if len(mob_stack) > 0:
            location = mob_stack.pop()

    # Player list comes as tuples with position info paired to the actor.
    for actor in player_stack:
        if actor[1] == 'pfrl':
            battle_grid['pfr']['left'] = actor[0]
        if actor[1] == 'pfrc':
            battle_grid['pfr']['center'] = actor[0]
        if actor[1] == 'pfrr':
            battle_grid['pfr']['right'] = actor[0]
        if actor[1] == 'pbrl':
            battle_grid['pbr']['left'] = actor[0]
        if actor[1] == 'pbrc':
            battle_grid['pbr']['center'] = actor[0]
        if actor[1] == 'pbrr':
            battle_grid['pbr']['right'] = actor[0]

    print(battle_grid)
    
    return battle_grid


