class Item(object):

    def __init__(self, config):
        """Create an interactive "item".
        :config: Item configuration data provided as dictionary.
        """
        self.description = config["description"]
        self.name = config["name"]
        self.generic_name = config["generic_name"]
        self.weight = config["weight"]
        self.min_dmg = config["min_dmg"]
        self.max_dmg = config["max_dmg"]
        self.element = config["element"]
        self.attacks = config["attacks"]
        self.range = config["range"]
        self.scope = config["scope"]
        self.is_equipped = False
        self.equip_slots = {
                "head": config["head"],
                "body": config["body"],
                "legs": config["legs"],
                "arms": config["arms"],
                "hands": config["hands"],
                "feet": config["feet"],
                "accessory": config["accessory"],
                "lhand": config["lhand"],
                "rhand": config["rhand"]
                }
