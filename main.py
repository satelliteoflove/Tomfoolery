import struct
import readline
from numpy import random
import collections
import yaml
import pprint
import items.weapon
import items.config
import party.party
import dm


# Begin initialization and presentation.
the_dm = dm.Dm()

# loop
while True:

    move = input(">").lower().split()
    for i, word in enumerate(move):
        print(word)     # print the command that was just entered
    if move[0] == 'q' or move[0] == "quit":
        break
    else:
       the_dm.parse_command(move)
