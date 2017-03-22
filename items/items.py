class Item(object):
    """ Root item class.
    Used as a parent to weapons, potions, helmets, rings, etc.
    """
    def __init__(self, config):
        self.weight = 1
        self.description = ""
        self.general_name = ""
        self.description = "It's an item"
        self.name = "item"
        self.is_equipped = False
        self.can_be_equipped = False
    def effect(self,target,damage,status):
        target = worldCharacters[target]
        damage = damage
        status_effect = status
        target.HP += damage
        target.status_effect += status
