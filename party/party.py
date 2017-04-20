class Party(object):
    """Class for storing characters in a group.
    """
    def __init__(self):
        self.xy_pos = (0,0)
        self.currentRoom = []
        self.members = []
        self.encounter_chance = 0.0

    def move(self, direction):
#        print("moving party..." + direction)
        for member in self.members:
#            print("value of member uuid: " + str(member.uuid))
#            print("member name: " + member.name)
            member.go(direction)

    def add_char(self, character):
        print("Current party members:")
        for char in self.members:
            print(char.name)
        self.members.append(character)
        print("Current party members:")
        for char in self.members:
            print(char.name)

    def rem_char(self, character):
        print("Current party members:")
        for char in self.members:
            print(char.name)
        self.members.remove(character)
        print("Current party members:")
        for char in self.members:
            print(char.name)

    def monster_encounter(self, party_weight, level):
        print("Encounter!")
        monster_party = MonsterParty(party_weight)
        print("You have encountered: ")
        for monster in monster_party.members:
            print(monster.name)

