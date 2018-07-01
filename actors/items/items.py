import effects

class Item(object):
    """ Root item class.
    """
    def __init__(self, config):
        self.description = config["description"]
        self.name = config["name"]

    def bind_type(self, itemtype):
        self.generic_name = itemtype["generic_name"]
        self.weight = itemtype["weight"]
        self.equippable = itemtype["equippable"]
        self.break_chance = itemtype["break_chance"]

    def bind_effect(self, effect):
        pass

    def bind_affix(self, effect):
        self.affix_effect = effect

    def bind_suffix(self, effect):
        self.suffix_effect = effect

class Weapon(Item):
    """All weapons can be described with this class."""
    def __init__(self, list_of_weapons, weapon_index):
        self.isweapon = True
        self.name = list_of_weapons[weapon_index]["name"]
        self.min_dmg = list_of_weapons[weapon_index]["min_dmg"]
        self.max_dmg = list_of_weapons[weapon_index]["max_dmg"]
        self.can_be_equipped = True
        self.is_equipped = False
        self.description = list_of_weapons[weapon_index]["description"]

