import struct
import readline
from numpy import random
import collections
import world.world
import world.config
import items.weapon
import items.config
import characters.pc
import characters.config
import mobs.mobs
import mobs.mobgroup
import mobs.config
import party.party

worldCharacters = []


# Begin initialization and presentation.

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

world1 = world.world.World(world.config.WORLD_CONFIG)
worldCharacters = world.config.worldCharacters

#In-town functions

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
player = characters.pc.Character()
#player2 = Character()
party1 = party.party.Party()
party1.add_char(player)

mobparty1 = mobs.mobgroup.MobGroup(1,mobs.config.MONSTER_CATALOG)

print("The following characters are in the world list:")
for character in worldCharacters:
    print(character.name)

# display "main menu"
showInstructions()

# loop
while True:

    move = input(">").lower().split()

    if move[0] == "go":
        party1.move(move[1])
    elif move[0] == "encounter":
        party1.monster_encounter(1,0)
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
        for character in worldCharacters:
            print(character.name)
    elif move[0] == "placeme":
        player.place_random()
    #elif move[1] == "place" and move[1] in rooms:
    #    player.place_room(move[1])
    elif move[0] == "attack" and move[1]:
        player.attack(move[1])
    elif move[0] == "look":
        player.view_surroundings()
    elif move[0] == "status":
        player.show_stats()
    elif move[0] == "addxp":
        player.add_xp(int(move[1]))
    elif move[0] == "levelup":
        player.level_up()
    elif move[0] == "help":
        showInstructions()
        dir(player)
    elif move[0] == "bonuspoints":
        player.bonusPoints = int(move[1])
    elif move[0] == "classchange":
        player.set_class()
#    elif move[0] == "abp":
#        player.assign_BonusPoints()
    elif move[0] == "q" or move[0] == "quit":
        break
    else:
        print("I have no idea what you're trying to do.")
