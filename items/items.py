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
        #TODO: implement item repair system
        #self.reparable = itemtype["reparable"]

    def bind_affix(self, effect):
        self.affix_effect = effect

    def bind_suffix(self, effect):
        self.suffix_effect = effect
