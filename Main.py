__author__ = 'Chris'

import random

races = {
    "elf" : {"strength":}
}

class Character(object):
    'Common base class for all PCs and NPCs.'
    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.strength = 8
        self.vitality = 8
        self.hitPoints = (self.vitality / 10) * random.randint(5,30)
        self.attack = 10
        self.bonusPoints = random.randint(5,25)
        self.defense = 1
        self.inventory = []

    def showStats(self):
        print(self.name + " Statistics:")
        print("STR: " + str(self.strength))
        print("VIT: " + str(self.vitality))
        print("HP: " + str(self.hitPoints))
        print("ATK: " + str(self.attack))
        print("DEF: " + str(self.defense))

def showInstructions():
    '''print a (temporary) "main menu", and the available commands'''
    print("WizardryClone")
    print("=============")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")


def showStatus(character):
    '''print the player's current status'''
    print("===================")
    print("You are in the " + rooms[currentRoom]["name"])
    character.showStats()
    print("Inventory: " + str(character.inventory))
    #list items, none if empty
    if "item" in rooms[currentRoom]:
        print("In the room, you see a " + rooms[currentRoom]["item"])

'''A dictionary representation of a single dungeon level'''
rooms = {
    1: { "name":"Hall",
         "east":2,
         "south":3},
    2: { "name":"Bedroom",
         "west":1,
         "south":4,
         "item":"sword"},
    3: { "name":"Kitchen",
         "north":1},
    4: { "name":"Bathroom",
         "north":2}
         }

#create character
player = Character()

#start the player off in a room
currentRoom = 1

#display "main menu"
showInstructions()

#loop
while True:

    showStatus(player)

    move = input(">").lower().split()

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way.")

    if move[0] == "get":
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            player.inventory += [move[1]]
            print(move[1] + " taken.")
            del rooms[currentRoom]["item"]
        else:
            print("You can't take " + move[1] + ".")