__author__ = 'Chris'

import random

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


class Character(object):
    'Common base class for all PCs and NPCs.'
    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.strength = 8
        self.vitality = 8
        self.hitPoints = int((self.vitality / 10) * random.randint(5,30))
        self.attack = 3
        self.bonusPoints = random.randint(5,25)
        self.defense = 1
        self.inventory = []
        #TODO: Equipment system
    def show_stats(self):
        print(self.name + " Statistics:")
        print("STR: " + str(self.strength))
        print("VIT: " + str(self.vitality))
        print("HP: " + str(self.hitPoints))
        print("ATK: " + str(self.attack))
        print("DEF: " + str(self.defense))
    def show_inventory(self):
        print("Inventory: " + str(self.inventory))
        #list items, none if empty
    def take_damage(self,damage):
        self.hitPoints -= damage
        print(self.name + " took " + str(damage) + " damage.")

def showInstructions():
    '''print a (temporary) "main menu", and the available commands'''
    print("WizardryClone")
    print("=============")
    print("Commands:")
    print("'go [direction]'")
    print("'get [item]'")
    print("'inventory'")
    print("'status'")


def view_surroundings(character):
    '''print the player's current status'''
    print("===================")
    print("You are in the " + rooms[currentRoom]["name"])
    if "description" in rooms[currentRoom]:
        print(rooms[currentRoom]["description"])
    if "items" in rooms[currentRoom]:
        for thing in rooms[currentRoom]["items"]:
            print("In the room, you see a " + thing.name + ".")

#Item initialization
sword1 = Sword()
item1 = Item()

#A single "dungeon" level
rooms = {
    1: { "name":"Hall",
         "description":"The hall is long, dark, and connects the Bedroom and Kitchen.",
         "east":2,
         "south":3},
    2: { "name":"Bedroom",
         "west":1,
         "south":4,
         "items":[sword1,item1]},
    3: { "name":"Kitchen",
         "description":"The kitchen, which once must have been beautiful and modern, is now a dingy shadow of its "
                       "former self.  Thick dust coats most surfaces, and motes of dust catch in your nose.",
         "north":1},
    4: { "name":"Bathroom",
         "north":2}
         }


#create characters, list of characters
player = Character()
enemy = Character()

character_list = [player,enemy]

#start the player off in a room
currentRoom = 1

#display "main menu"
showInstructions()

#loop
while True:

    move = input(">").lower().split()

    if len(move) == 0:
        print("...")
    if len(move) > 0:
        if move[0] == "go":
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
                view_surroundings(player)
            else:
                print("You can't go that way.")
        elif move[0] == "get":
            #print(rooms[currentRoom]["items"][0].name)
            temp_item_list = []
            for item in rooms[currentRoom]["items"]:
                temp_item_list.append(item.name)
            if "items" in rooms[currentRoom] and move[1] in temp_item_list:
                for item in rooms[currentRoom]["items"]:
                    if move[1] == item.name:
                        player.inventory.append(item)
                        print(move[1] + " taken.")
                        rooms[currentRoom]["items"].remove(item)
            else:
                print("You can't take " + move[1] + ".")
        elif move[0] == "drop":
            if move[1] in player.inventory:
                print("You drop the " + move[1])
        elif move[0] == "attack":
            player.take_damage(enemy.)
        elif move[0] == "inventory":
            player.show_inventory()
        elif move[0] == "look":
            view_surroundings(player)
        elif move[0] == "status":
            player.show_stats()
        elif move[0] == "q" or move[0] == "quit":
            break
        else:
            print("I have no idea what you're trying to do.")