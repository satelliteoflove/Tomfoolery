class Store(object):
    """Buy, sell, identify and remove cursed items."""
    def __init__(self):
        """Standard Store object for feeding items."""
        self.inventory = {}

    def buy_item(self, item):
        self.inventory[item.uuid] = item
        return item.sell_value

    def sell_item(self, item, available_money):
        funds = available_money
        if funds >= item.sell_price:
            self.inventory[item.uuid].__delitem__()
            return item.sell_price
        else:
            return False
