# Module for combat helper methods


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

    for position in mfr:
        if len(mob_stack) > 0:
            if mfr[0] is None:
                mfr[0] = mob_stack.pop()
        if len(mob_stack) > 0:
            if mfr[1] is None:
                mfr[1] = mob_stack.pop()
        if len(mob_stack) > 0:
            if mfr[2] is None:
                mfr[2] = mob_stack.pop()

    # Add entries for mbr and mrr

    for position in pfr:
        if len(player_stack) > 0:
            if pfr[0] is None:
                pfr[0] = player_stack.pop()
        if len(player_stack) > 0:
            if pfr[1] is None:
                pfr[1] = player_stack.pop()
        if len(player_stack) > 0:
            if pfr[2] is None:
                pfr[2] = player_stack.pop()

    # Add entries for pbr

    return battle_grid


