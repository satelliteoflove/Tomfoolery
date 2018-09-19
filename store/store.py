class Store(object):
    def __init__(self):
        self.inventory = {}
        self.current_player = None
        self.current_party = None

    def pool_gold(self):
       self.current_party.pool_gold(current_player) 

    def buy_item(self, item):
        self.inventory[item.uuid] = item
        return item.sell_value

    def sell_item(self, item):
        self.inventory[item.uuid]