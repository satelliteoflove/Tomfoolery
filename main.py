import struct
import readline
from numpy import random
import collections
import yaml
import pprint
import world.world
import world.config
import items.weapon
import items.config
import characters.pc
import characters.config
import party.party
from commpar import commpar
from dm import dm

worldCharacters = []

# Begin initialization and presentation.
#TODO: What can be done to generate this list from available data?
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

the_dm = dm.Dm()
player = the_dm.make_pc()

worldCharacters = world.config.worldCharacters


# Item initialization - item names are case sensitive for now
claws2 = items.weapon.Weapon(items.config.WEAPON_BASE_TYPES,1)

# Four rooms for testing other functions.
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
             "items": [claws2],
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

# create characters, list of characters
#player = characters.pc.Character()

#player2 = Character()
party1 = party.party.Party()
party1.add_char(player)
party1.rem_char(player)

# display "main menu"
showInstructions()

# initialize command parser
commparser = commpar.Commpar()

# loop
while True:

    move = input(">").lower().split()
    if move[0] == 'q' or move[0] == "quit":
        break
    else:
       commparser.parse_command(move)
