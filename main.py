__author__ = 'Chris'

import random
import math
import numpy
import curses



#Globals
world_characters = []
MAP_WIDTH = 50
MAP_HEIGHT = 50

min_room_width = 1
min_room_height = 1
max_room_width = 3
max_room_height = 3


class Item(object):
    def __init__(self):
        self.weight = 1
        self.description = ""
        self.general_name = ""
        self.description = "It's an item"
        self.name = "item"

class Weapon(Item):
    def __init__(self):
        self.isweapon = True
        self.name = "item"

class Sword(Weapon):
    def __init__(self):
        self.min_dmg = 1
        self.max_dmg = 5
        self.description = "It is a sword."
        self.long_description = "This is a simple sword made of steel."
        self.name = "sword"

class Room(object):
    def __init__(self, x1, y1, width, height):
        self.exits = ["east", "west", "south", "north"]
        self.name = "Room"
        self.description = "A basic room."
        self.long_description = "This base type room has no special description."
        self.characters = []
        self.items = []
        self.width = width
        self.height = height
        self.x1 = x1
        self.x2 = x1 + self.width
        self.y1 = y1
        self.y2 = y1 + self.height
        self.center = (round((math.floor(self.x1 + self.x2) / 2)), round((math.floor(self.y1 + self.y2) / 2)))

    def intersects(self, room):
        return (self.x1 <= room.x2 and self.x2 >= room.x1 and
                self.y1 <= room.y2 and self.y2 >= room.y1)

class T_Room(Room):
    '''"T"-shaped room. Default has exits to the east, west, and south.'''

    def __init__(self):
        self.exits = ["east", "west", "south"]

    def __init__(self, isReversed):
        self.isReversed = isReversed
        if isReversed == True:
            self.exits = ["east", "west", "north"]



class Character(object):
    """Common base class for all PCs and NPCs."""
    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.strength = 8
        self.vitality = 8
        self.hitPoints = int((self.vitality / 10) * random.randint(5,30))
        self.attack = 3
        self.bonusPoints = random.randint(5,25)
        self.defense = 1
        self.inventory = []
        self.currentRoom = 1
        self.add_to_room()
        world_characters.append(self)
        self.equipment = []
    def add_to_room(self):
        for chamber in rooms:
            if chamber == self.currentRoom:
                rooms[self.currentRoom]["characters"].append(self)
    def show_stats(self):
        print(self.name + " Statistics:")
        print("STR: " + str(self.strength))
        print("VIT: " + str(self.vitality))
        print("HP: " + str(self.hitPoints))
        print("ATK: " + str(self.attack))
        print("DEF: " + str(self.defense))
    def show_inventory(self):
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(item.name)
        else:
            print("You aren't carrying anything.")
        #list items, none if empty
    def place_random(self):
        #start the player off in a room
        self.currentRoom = random.randint(1,len(rooms))
    def place_room(self, room:int):
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
        for dude in current_room_character_list:
            print(dude.name)
    def go(self,newroom):
        if move[1] in rooms[self.currentRoom]:
            rooms[self.currentRoom]["characters"].remove(self)
            self.currentRoom = rooms[self.currentRoom][move[1]]
            rooms[self.currentRoom]["characters"].append(self)
            self.view_surroundings()
        else:
            print("You can't go that way.")
    def get(self,item_to_get):
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
    def drop(self,item_to_drop):
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

def party_add_character(character_type,n):
    """Creates a list of Character objects"""

#Item initialization
sword1 = Sword()
item1 = Item()


def Zero_Tiles():
    # Creates a zeroed/impassible grid of tiles.
    zeroed_tiles = [[0 for x in range(5)] for y in range(5)]
    return zeroed_tiles


print(Zero_Tiles())

room1 = Room(1, 1, 2, 5)

print(room1.center)


def place_rooms():
    rooms = [[Room(random.randint(1, MAP_WIDTH - 1), random.randint(1, MAP_HEIGHT - 1),
                   random.randint(min_room_width, max_room_width),
                   random.randint(min_room_height, max_room_height))
              for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]



#A single "dungeon" level
rooms = {
    1: { "name":"Hall",
         "description":"The hall is long, dark, and connects the Bedroom and Kitchen.",
         "east":2,
         "south":3,
         "items":[],
         "characters":[]},
    2: { "name":"Bedroom",
         "description": "The bedroom is a simple affair, with a chair in one corner and a bed in the middle of the "
                        "east wall.",
         "west":1,
         "south":4,
         "items":[sword1,item1],
         "characters":[]},
    3: { "name":"Kitchen",
         "description":"The kitchen, which once must have been beautiful and modern, is now a dingy shadow of its "
                       "former self.  Thick dust covers everything.",
         "north":1,
         "items":[],
         "characters":[]},
    4: { "name":"Bathroom",
         "description": "This bathroom has seen better days.  The mirror on the vanity is cracked, the bathtub is "
                        "irreversibly stained, and the tile is worn and filthy.",
         "north":2,
         "items":[],
         "characters":[]}
         }

#create characters, list of characters
player = Character()

#display "main menu"
showInstructions()

# list of words understood by the game paired with their respective methods.
words = ["go", "get", ""]

#loop
while True:

    move = input(">").lower().split()

    if move[0] == "go":
        player.go(move[1])
    elif move[0] == "get":
        player.get(move[1])
    elif move[0] == "inventory":
        player.show_inventory()
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
    '''
        elif move[0] == "attack":
            print("Not yet implemented.")
        elif move[0] == "look":
            view_surroundings(player)
        elif move[0] == "status":
            player.show_stats()
        elif move[0] == "q" or move[0] == "quit":
            break
        else:
            print("I have no idea what you're trying to do.")
    '''

    if move[0] == "q" or move[0] == "quit":
        break
