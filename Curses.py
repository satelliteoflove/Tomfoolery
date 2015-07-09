__author__ = 'Chris'

import random, math

#constants
dice_minimum = 6
dice_maximum = 25

base_str = 6
base_dex = 6
base_int = 6
base_con = 6

#methods
def available_classes(strength,dexterity,intelligence):
    fighter_available = "False"
    thief_available = "False"
    mage_available = "False"

    if strength > 9:
        fighter_available = "True"
    elif dexterity > 9:
        thief_available = "True"
    elif intelligence > 9:
        mage_available = "True"

    return (fighter_available,thief_available,mage_available)

def bonus_point_distribution(strength, dexterity, intelligence, constitution):
    bonus_points_total = random.randint(dice_minimum,dice_maximum)
    while bonus_points_total > 0:
        print("Bonus Points: " + str(bonus_points_total))
        print("Current stats:\n"
              "STR = {0}\n"
              "DEX = {1}\n"
              "INT = {2}\n"
              "CON = {3}\n".format(strength,dexterity,intelligence,constitution))
        choice = input("Distribute your bonus points to open class choices.\n"
          "Choose (S)trength, (D)exterity, (I)ntelligence, or (C)onstitution")[:1].lower()
        if choice == "s":
            strength += 1
            bonus_points_total -= 1
        elif choice == "d":
            dexterity += 1
            bonus_points_total -= 1
        elif choice == "i":
            intelligence += 1
            bonus_points_total -= 1
        elif choice == "c":
            constitution += 1
            bonus_points_total -= 1

        fighter_available,thief_available,mage_available = available_classes(strength,dexterity,intelligence)
        print("The following classes are available:\n")
        print("Fighter: {0}\n"
              "Thief: {1}\n"
              "Mage: {2}".format(fighter_available,thief_available,mage_available))

        return (strength,dexterity,intelligence,constitution)

def generate_character(strength,dexterity,intelligence,constitution):
    #name = input("What is your name?\n")
    bonus_point_distribution(strength,dexterity,intelligence,constitution)

    generator_choice = input("Accept these values? (y/n)")[1:].lower()
    if generator_choice == "y":
        return (strength,dexterity,intelligence,constitution)
    elif generator_choice == "n":
        bonus_point_distribution(base_str,base_dex,base_int,base_con)


#main logic

player_str,player_dex,player_int,player_con = generate_character(base_str,base_dex,base_int,base_con)
