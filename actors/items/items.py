class Item(object):

    def __init__(self, config):
        """
        :config: Item configuration data provided as dictionary.
        """
        self.description = config["description"]
        self.name = config["name"]
        self.generic_name = config["generic_name"]
        self.weight = config["weight"]
        self.allowed_slots = config["allowed_slots"]
        self.min_dmg = config["min_dmg"]
        self.max_dmg = config["max_dmg"]
        self.element = config["element"]
        self.attacks = config["attacks"]
        self.range = config["range"]
        self.scope = config["scope"]
        self.is_equipped = False
