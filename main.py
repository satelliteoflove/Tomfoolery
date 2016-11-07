__author__ = 'Chris'

import random

# Globals
world_characters = []
MAP_WIDTH = 0
MAP_HEIGHT = 0


class Item(object):
    def __init__(self):
        self.weight = 1
        self.description = ""
        self.general_name = ""
        self.description = "It's an item"
        self.name = "item"
        self.is_equipped = False
        self.can_be_equipped = False


class Weapon(Item):
    """All weapons can be described with this class."""

    def __init__(self, name, min_dmg, max_dmg, description):
        self.isweapon = True
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.can_be_equipped = True
        self.is_equipped = True
        self.description = description


class Character(object):
    """Common base class for all PCs and NPCs."""

    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.strength = 8
        self.vitality = 8
        self.hitPoints = int((self.vitality / 10) * random.randint(5, 30))
        self.attack = 1
        self.bonusPoints = random.randint(5, 25)
        self.defense = 1
        self.inventory = []
        self.currentRoom = (0, 0)
        self.add_to_room()
        self.direction = "north"
        world_characters.append(self)
        self.equipment = []

    def add_to_room(self):
        for chamber in rooms:
            if chamber == self.currentRoom:
                rooms[self.currentRoom]["characters"].append(self)

    def show_stats(self):
        """Displays current character stats."""
        print("Statistics for " + self.name)
        print("STR: " + str(self.strength))
        print("VIT: " + str(self.vitality))
        print("HP: " + str(self.hitPoints))
        print("ATK: " + str(self.attack))
        print("DEF: " + str(self.defense))

    def show_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item.is_equipped == True:
                    print("#" + item.name)
                else:
                    print(item.name)
        else:
            print("You aren't carrying anything.")
            # list items, none if empty

    def place_random(self):
        # start the player off in a room
        self.currentRoom = random.randrange()

    def place_room(self, room: int):
        if room > 0 and room <= len(rooms):
            self.currentRoom = room

    def view_surroundings(self):
        """print what the player can see"""
        currentRoom = self.currentRoom
        current_room_character_list = []
        print("===================")
        print("You are in the " + rooms[currentRoom]["name"])
        if "description" in rooms[currentRoom]:
            print(rooms[currentRoom]["description"])
        if "items" in rooms[currentRoom]:
            for thing in rooms[currentRoom]["items"]:
                print("In the room, you see a " + thing.name + ".")
        for room_character in rooms[self.currentRoom]["characters"]:
            current_room_character_list.append(room_character)
        print("Nearby, you see " + str(len(current_room_character_list)) + " characters:")
        for character in current_room_character_list:
            print(character.name)
        print("Exits:")
        if "north" in rooms[currentRoom]:
            print("North")
        if "south" in rooms[currentRoom]:
            print("South")
        if "east" in rooms[currentRoom]:
            print("East")
        if "west" in rooms[currentRoom]:
            print("West")

    def go(self, newroom):
        if move[1] in rooms[self.currentRoom]:
            rooms[self.currentRoom]["characters"].remove(self)
            self.currentRoom = rooms[self.currentRoom][move[1]]
            rooms[self.currentRoom]["characters"].append(self)
            self.view_surroundings()
        else:
            print("You can't go that way.")

    def get(self, item_to_get):
        temp_item_list = []
        for item in rooms[self.currentRoom]["items"]:
            temp_item_list.append(item.name)
        if "items" in rooms[self.currentRoom] and item_to_get in temp_item_list:
            for item in rooms[self.currentRoom]["items"]:
                if item_to_get == item.name:
                    self.inventory.append(item)
                    print(item.name + " taken.")
                    rooms[self.currentRoom]["items"].remove(item)
        else:
            print("You can't take " + item_to_get + ".")

    def drop(self, item_to_drop):
        temp_item_list = []
        for item in self.inventory:
            temp_item_list.append(item.name)
        if item_to_drop in temp_item_list:
            for item in self.inventory:
                if item_to_drop == item.name:
                    rooms[self.currentRoom]["items"].append(item)
                    print(item.name + " dropped.")
                    self.inventory.remove(item)
        else:
            print("Drop what, again?")

    def equip(self, item_to_equip):
        temp_item_list = []
        for item in self.inventory:
            temp_item_list.append(item.name)
        if item_to_equip in temp_item_list:
            for item in self.inventory:
                if item_to_equip == item.name and item.can_be_equipped is True:
                    item.is_equipped = True
                    print(item.name + " equipped.")


# TODO: Create "go" method which uses the current direction and moves char/npc there.
class NonPlayerCharacter(Character):
    """Common base class for all NPCs."""

    def __init__(self, name):
        self.name = name
        self.strength = 3
        self.vitality = 3
        self.hitPoints = int((self.vitality / 10) * random.randint(5, 30))
        self.attack = 1
        self.defense = 1
        self.inventory = []
        self.currentRoom = (0, 0)
        self.add_to_room()
        world_characters.append(self)
        self.equipment = []
        self.movement = 1
        self.direction = "north"

    def change_direction(self):
        directions = ["north", "south", "east", "west"]
        directions.remove(self.direction)
        self.direction = random.choice(directions)

    # def go(self, newroom):
    #     if move[1] in rooms[self.currentRoom]:
    #         rooms[self.currentRoom]["characters"].remove(self)
    #         self.currentRoom = rooms[self.currentRoom][move[1]]
    #         rooms[self.currentRoom]["characters"].append(self)
    #         self.view_surroundings()
    #     else:
    #         print("You can't go that way.")


def showInstructions():
    """print a (temporary) "main menu", and the available commands"""
    print("WizardryClone")
    print("=============")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'drop [item]'")
    print("'inventory'")
    print("'status'")
    print("'look'")
    print("'attack'")


def party_add_character(character_type, n):
    """Creates a list of Character objects"""


# Item initialization - item names are case sensitive for now
sword1 = Weapon("sword", 1, 5, "This is a simple short sword of steel.")
item1 = Item()

# A single "dungeon" level
rooms = {
    (0, 0): {"name": "0,0",
             "description": "0,0",
             "east": (1, 0),
             "north": (0, 1),
             "items": [],
             "characters": []},
    (0, 1): {"name": "0,1",
             "description": "0,1",
             "south": (0, 0),
             "east": (1, 1),
             "items": [sword1, item1],
             "characters": []},
    (1, 0): {"name": "1,0",
             "description": "1,0",
             "north": (1, 1),
             "west": (0, 0),
             "items": [],
             "characters": []},
    (1, 1): {"name": "1,1",
             "description": "1,1",
             "south": (1, 0),
             "west": (0, 1),
             "items": [],
             "characters": []}
}

# A list of weapons
weapons = {
    "sword01": {"name": "Short Sword"}
}

# create characters, list of characters
player = Character()
goblin = NonPlayerCharacter("goblin")
orc = NonPlayerCharacter("orc")

# display "main menu"
showInstructions()

# loop
while True:

    move = input(">").lower().split()

    if move[0] == "go":
        player.go(move[1])
    elif move[0] == "get" or move[0] == "take":
        player.get(move[1])
    elif move[0] == "inventory":
        player.show_inventory()
    elif move[0] == "equip":
        player.equip(move[1])
    elif move[0] == "drop":
        player.drop(move[1])
    elif move[0] == "look":
        player.view_surroundings()
    elif move[0] == "list":
        for character in world_characters:
            print(character.name)
    elif move[0] == "placeme":
        player.place_random()
    elif move[0] == "place" and move[1] in rooms:
        player.place_room(move[1])
    elif move[0] == "attack":
        print("Not yet implemented.")
    elif move[0] == "look":
        player.view_surroundings()
    elif move[0] == "status":
        player.show_stats()
    else:
        print("I have no idea what you're trying to do.")

    if move[0] == "q" or move[0] == "quit":
        break

    for character in world_characters:
        if isinstance(character, NonPlayerCharacter):
            print(character.name + " changes direction.")
            character.change_direction()
            print(character.name + " is now pointing %s" %character.direction)
            character.go(character.direction)