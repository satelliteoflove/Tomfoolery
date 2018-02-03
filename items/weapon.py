from . import items

class Weapon(items.Item):
    """All weapons can be described with this class."""
    def __init__(self, list_of_weapons, weapon_index):
        """

        Args:
            list_of_weapons:
            weapon_index:
        """
        self.isweapon = True
        self.name = list_of_weapons[weapon_index]["name"]
        self.min_dmg = list_of_weapons[weapon_index]["min_dmg"]
        self.max_dmg = list_of_weapons[weapon_index]["max_dmg"]
        self.can_be_equipped = True
        self.is_equipped = False
        self.description = list_of_weapons[weapon_index]["description"]

