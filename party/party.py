class Party(object):
    """Class for storing characters in a group.
    """
    def __init__(self):
        self.xy_pos = (0,0)
        self.members = {}
        self.encounter_chance = 0.0
        self.max_size = 6
        self.current_size = 0
        self.formation = {
                'front': {'left': False, 'middle': False, 'right': False},
                'back': {'left': False, 'middle': False, 'right': False}
                }

    def add_char(self, character):
        print("Adding member:" + character.name)
        self.members[character.name] = character
        print("Current party members:")
        for char in self.members.values():
            print(char.name)

    def set_formation(self):
        print("The following party members can be arranged:")
        for actor in self.members.values():
            print(actor.name)
        print("And the party is currently arranged as:")
       #TODO: formation arrangement 

    def rem_char(self, character):
        print("Removing member:")
        for char in self.members:
            print(char.name)
        self.members.remove(character)
        print("Current party members:")
        for char in self.members:
            print(char.name)
