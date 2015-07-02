__author__ = 'Chris'

import random

statusAilments = {}

races = {"Elf": (6,8), "Dwarf": (10,8), "Human": (8,8)}
'The "races" dictionary contains each race, with the following stats pre-defined:' \
'   strength' \
'   vitality' \
'example: dict = {"Key1": (ValX1, ValY1, ValZ1), "Key2": (ValX2, ValY2, ValZ2),...,"Key99": (ValX99, ValY99, ValY99)}'

class Character(object):
    'Common base class for all PCs and NPCs.'
    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.hitPoints = random.randint(5,30)
        self.attack = 10
        self.bonusPoints = random.randint(5,25)
        self.strength = 8
        self.vitality = 8
        self.defense = 1


def MakeCharacter():
    playerchar = Character()
    print("Name: %s     Points To Spend: %s" % (playerchar.name, playerchar.bonusPoints))
    print("Strength: %s   Vitality: %s" % (playerchar.strength, playerchar.vitality))
    choice1 = input("Spend points on (S)trength, or (V)itality?")
    while playerchar.bonusPoints > 0:
        if choice1 == "S":
            choice2 = input("How many points?")
            if choice2 <= playerchar.bonusPoints and choice2 > 0:
                playerchar.strength += choice2
                playerchar.bonusPoints -= choice2
            #elif choice2 < 0:

print(races['Elf'])
MakeCharacter()