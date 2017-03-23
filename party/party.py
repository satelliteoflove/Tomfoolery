class Party(object):
    """Class for storing characters in a group.
    """
    def __init__(self):
        self.xy_pos = (0,0)
        self.currentRoom = []
        self.members = {}
        self.encounter_chance = 0.0

    def add_char(self, character):
        print("Current members:")
        list(self.members)
        self.members[character.uuid] = character
        list(self.members)

    def move(self, direction):
        print("moving party..." + direction)
        for member in self.members.values():
            print("value of member uuid: " + str(member.uuid))
            print("member name: " + member.name)
            member.go(direction)
        next(iter(self.members.values())).view_surroundings()

    def rem_char(self, character):
        print("Current members:")
        list(self.members)
        self.members[character.uuid].remove()
        list(self.members)

    def monster_encounter(self, party_weight, level):
        print("Encounter!")
        monster_party = MonsterParty(party_weight)
        print("You have encountered: ")
        for monster in monster_party.members:
            print(monster.name)

