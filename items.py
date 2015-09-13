__author__ = 'Chris'

class Items:
    def __init__(self):
        self.weight = 1
        self.description = ""
        self.general_name = ""

class Weapons(Items):
    def __init__(self):
        self.isweapon = True
        self.mindamage = 1
        self.maxdamage = 5
