class Party(object):
    """Class for storing characters in a group.
    """
    def __init__(self):
        self.xy_pos = (0,0)
        self.currentRoom = []
        self.members = {}
        self.encounter_chance = 0.0
        self.max_size = 6
        self.current_size = 0

    def add_char(self, character):
        print("Adding member:" + character.name)
        self.members[character.name] = character
        print("Current party members:")
        for char in self.members.values():
            print(char.name)

    def rem_char(self, character):
        print("Removing member:")
        for char in self.members:
            print(char.name)
        self.members.remove(character)
        print("Current party members:")
        for char in self.members:
            print(char.name)
