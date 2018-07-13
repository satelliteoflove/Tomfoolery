from numpy import random
from uuid import uuid4
from . import config
import collections
from actors.items.effects import effect

class Character(object):
    """Common base class for all PCs and NPCs."""

    def __init__(self):
        """Creates a playable character."""
        self.name = self.set_name()
        self.uuid = uuid4()
        self.currentLevel = 1
        self.currentXP = 0
        # statNames is only used in a helper function to determine if a named
        # stat is legitimate. This will likely be unnecessary after input is
        # driven by something other than the command interpreter.
        self.statNames = ["strength", "agility", "vitality", "intelligence",
                           "piety", "luck"]
        self.strength = 0
        self.agility = 0
        self.vitality = 0
        self.intelligence = 0
        self.piety = 0
        self.luck = 0
        self.set_race()
        self.set_sex()
        self.set_bonusPoints()
        self.set_class()
        self.assign_BonusPoints()
        self.set_xp_rate()
        self.set_initial_HP()
        self.set_class_AC() #As in characters.md - AD&D rules for AC/THAC0.
        self.set_THAC0()
        self.inventory = {}
        self.equipment = {"head":0, "body":0, "legs":0,
                "arms":0, "hands":0, "feet":0, "accessory":0,
                "lhand": 0, "rhand": 0}
        self.position = (0, 0)
        self.set_AP()
        self.action_list = {}
        self.type = False

    def show_inventory(self):
        # list items, none if empty
        if len(self.inventory) > 0:
            for k in self.inventory.keys():
                print(k)
        else:
            print("You aren't carrying anything.")

    def equip_item(self):
        """Equip item from inventory."""
        print("Choose a slot to equip.")
        for k in self.equipment.keys():
            print(k)
        choice = input()

        if self.equipment[choice]:
            print("Equip which item?")
            self.show_inventory()

    def set_class_AC(self):
        """Set character's class-based AC "base"."""
        self.AC = config.char_class_traits[self.char_class]["AC"]

    def set_THAC0(self):
        """Set character's class-based THAC0 "base"."""
        self.THAC0 = 20 - round((self.currentLevel *
                           config.char_class_traits[self.char_class]
                                 ["THAC0mult"]))

    def set_initial_HP(self):
        """Used to set *initial* HP for character.

        Depending on the character's class, a different amount of starting HP
        may be generated. A minimum of 2HP will be assigned to any starting
        character.

        TODO: Adjust vitality modifier for HP. There should be a "curve", where
        characters with especially low vitality get a penalty and high vitality
        grants a bonus, but this should be mild (not a multiplier based on
        vitality?).
        """
        self.hitPoints = 0
        self.maxHitPoints = 0
        chance = random.randint(0,1)

        if self.char_class == "samurai":
            if chance == 0:
                self.hitPoints = int(16 + self.vitality // 2)
            if chance == 1:
                self.hitPoints = (9 * (16 + self.vitality // 2) // 10)
        elif self.char_class == "fighter" or self.char_class == "lord":
            if chance == 0:
                self.hitPoints = 10 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (10 + self.vitality // 2) // 10)
        elif self.char_class == "priest":
            if chance == 0:
                self.hitPoints = 8 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (8 + self.vitality // 2) // 10)
        elif self.char_class == "thief" or self.char_class == "ninja":
            if chance == 0:
                self.hitPoints = 6 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self.vitality // 2) // 10)
        elif self.char_class == "bishop":
            if chance == 0:
                self.hitPoints = 6 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self.vitality // 2) // 10)
        elif self.char_class == "mage":
            if chance == 0:
                self.hitPoints = 4 + self.vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (4 + self.vitality // 2) // 10)

        if self.hitPoints < 2:
            self.hitPoints = 2

        self.maxHitPoints = self.hitPoints

    def add_maxHP(self):
        """Adds max HP when character gains a level.

        TODO: Ensure that vitality modifies added maximum HP.
        """
        if self.char_class == "fighter" or self.char_class == "lord":
            self.maxHitPoints += int(random.triangular(0,10,5))
        elif self.char_class == "priest" or self.char_class == "samurai":
            self.maxHitPoints += int(random.triangular(0,8,4))
        elif self.char_class == "monk":
            self.maxHitPoints += int(random.triangular(0,8,5))
        elif self.char_class == "thief" or self.char_class == "ninja":
            self.maxHitPoints += int(random.triangular(0,6,3))
        elif self.char_class == "bishop":
            self.maxHitPoints += int(random.triangular(0,6,3))
        elif self.char_class == "mage":
            self.maxHitPoints += int(random.triangular(0,4,2))

    def set_sex(self):
        """Sets the sex of the character.

        The sex of a character grants a one-time stat bonus upon character
        creation (+1 VIT (F)/+1 STR (M)), and only women can be valkyries.
        """
        #Quick hack
        self.sex = "male"

        #self.sex = ""
        while self.sex != "male" and self.sex != "female":
            print("What is the sex of the character?\n(male or female)")
            self.sex = input().lower()
        if self.sex == "male":
            self.strength += 1
        elif self.sex == "female":
            self.vitality += 1

    def set_bonusPoints(self):
        """Assigns starting bonus points.
        """
        self.bonusPoints = 0
        while self.bonusPoints < 4:
            self.bonusPoints = int(random.normal(8, 4))
        print("Bonus Points = " + str(self.bonusPoints))

    def set_race(self):
        """Used on character creation to set race values.

        After choosing a race, the minimum stat values are set for the character
        based on racial minimums.  In addition, any special fields such as
        resistance values or special attacks are set.
        """
        print("What race is this character?\nChoose from the following:")
        for key in config.char_race_traits.keys():
            print(key)
        #Quick hack
        self.race = "human"

        #self.race = ""
        while self.race == "":
            tryrace = input().lower()
            if tryrace in config.char_race_traits:
                self.race = tryrace
            else:
                print("That is not a valid race.")
                print("What race is this character?\nChoose from the following:")
                for key in config.char_race_traits.keys():
                    print(key)
        self.strength = config.char_race_traits[self.race]["min_str"]
        self.vitality = config.char_race_traits[self.race]["min_vit"]
        self.agility = config.char_race_traits[self.race]["min_agi"]
        self.intelligence = config.char_race_traits[self.race]["min_int"]
        self.piety = config.char_race_traits[self.race]["min_pie"]
        self.luck = config.char_race_traits[self.race]["min_luk"]

    def set_name(self):
        name_accepted = False
        while name_accepted == False:
            try_name = input("What is the player's name?\n")
            if len(try_name) > 12:
                print("Name is too long. Must be 12 characters or less.")
            else:
                name_accepted = True
        return try_name

    def validate_class(self, newclass):
        """Validates that a class can be chosen for the character by comparing
        total bonus points required vs current bonus points.
        """
        points_required = 0
        str_req = config.char_class_traits[newclass]["min_str"]
        agi_req = config.char_class_traits[newclass]["min_agi"]
        vit_req = config.char_class_traits[newclass]["min_vit"]
        int_req = config.char_class_traits[newclass]["min_int"]
        pie_req = config.char_class_traits[newclass]["min_pie"]
        luk_req = config.char_class_traits[newclass]["min_luk"]

        if str_req > self.strength:
            points_required += str_req - self.strength
        if agi_req > self.agility:
            points_required += agi_req - self.agility
        if vit_req > self.vitality:
            points_required += vit_req - self.vitality
        if pie_req > self.piety:
            points_required += pie_req - self.piety
        if luk_req > self.luck:
            points_required += luk_req - self.luck

        #sums all "min_stat"-type key values
        #for key, value in config.char_class_traits[newclass].items():
        #    if key.startswith('min_'):
        #
        #        points_required += value
        #        print(str(points_required))
        if points_required > self.bonusPoints:
            return False
        else:
            return True

    def set_class(self):
        """Modifications specific to class changes.

        Includes statistic changes, class variable update, etc.
        In addition, the rate of HP growth is defined here.
        """
        classlist = []
        for classname in config.char_class_traits.keys():
            if self.validate_class(classname):
                print(classname)
                classlist.append(classname)
        print("The following classes are available: ")
        print(classlist)
        try_class = input().lower()
        satisfied = False
        while satisfied == False:
            if try_class not in classlist:
                print("That class isn't in the list. Try again.")
                try_class = input().lower()
            else:
                self.char_class = try_class
                satisfied = True
                str_req = config.char_class_traits[try_class]["min_str"]
                agi_req = config.char_class_traits[try_class]["min_agi"]
                vit_req = config.char_class_traits[try_class]["min_vit"]
                int_req = config.char_class_traits[try_class]["min_int"]
                pie_req = config.char_class_traits[try_class]["min_pie"]
                luk_req = config.char_class_traits[try_class]["min_luk"]

                if str_req > self.strength:
                    self.bonusPoints -= str_req - self.strength
                    self.strength = str_req
                if agi_req > self.agility:
                    self.bonusPoints -= agi_req - self.agility
                    self.agility = agi_req
                if vit_req > self.vitality:
                    self.bonusPoints -= vit_req - self.vitality
                    self.vitality = vit_req
                if pie_req > self.piety:
                    self.bonusPoints -= pie_req - self.piety
                    self.piety = pie_req
                if luk_req > self.luck:
                    self.bonusPoints -= luk_req - self.luck
                    self.luck = luk_req

    def assign_BonusPoints(self):
        print("There are " + str(self.bonusPoints) + " remaining BP.")
        print("Your current statistics are: ")
        print("[S]trength: " + str(self.strength))
        print("[A]gility: " + str(self.agility))
        print("[V]itality: " + str(self.vitality))
        print("[I]ntelligence: " + str(self.intelligence))
        print("[P]iety: " + str(self.piety))
        print("[L]uck: " + str(self.luck))
        while self.bonusPoints > 0:
            stat_increased = 's'
#            stat_increased = input().lower()
            if stat_increased == 's':
                stat_increased = "strength"
            elif stat_increased == 'a':
                stat_increased = "agility"
            elif stat_increased == 'v':
                stat_increased = "vitality"
            elif stat_increased == 'i':
                stat_increased = "intelligence"
            elif stat_increased == 'p':
                stat_increased = "piety"
            elif stat_increased == 'l':
                stat_increased = "luck"

            if stat_increased not in self.statNames:
                print("That isn't a stat. Try again.")
            else:
                setattr(self, stat_increased, getattr(self, stat_increased) + 1)
                self.bonusPoints -= 1
                print("Bonus Points = " + str(self.bonusPoints))
                print("Strength: " + str(self.strength))
                print("Agility: " + str(self.agility))
                print("Vitality: " + str(self.vitality))
                print("Intelligence: " + str(self.intelligence))
                print("Piety: " + str(self.piety))
                print("Luck: " + str(self.luck))
        print("You don't have any bonus points left.")

    def set_xp_rate(self):
        """Sets the experience multiplier for a given race/class combination.
        """
        print("Setting xp rate multiplier.")
        print("self.char_class = " + self.char_class)
        print("self.race = " + self.race)
        print("My 'rate' is: " + str(
                            config.char_race_xp_rate[self.race][self.char_class]))
        if self.race in config.char_race_xp_rate:
            if self.char_class in config.char_race_xp_rate[self.race]:
                self.rate = config.char_race_xp_rate[self.race][self.char_class]
            else:
                print("That class doesn't exist for that race.")
        else:
            print("That race isn't in the list of xp rates.")

    def set_AP(self):
        """AP is a function of strength, which may change upon gaining a level.

        AP is a basic per-hit damage modifier.  Characters with very low
        strength have a damage penalty, whereas characters with very high
        strength have a damage bonus.
        """
        self.AP = 0
        if self.strength == 3:
            self.AP -= 3
        if self.strength == 4:
            self.AP -= 2
        if self.strength == 5:
            self.AP -= 1
        if self.strength > 15:
            self.AP += 1 * (self.strength - 15)
        if self.AP < 0:
            self.AP = 0
        print("This character's AP is: " + str(self.AP))

    def add_to_room(self):
        for chamber in rooms:
            if chamber == self.currentRoom:
                rooms[self.currentRoom]["characters"].append(self)

    def return_stats(self):
        return collections.OrderedDict(vars(self))

    def get_item(self, item):
        """PC gets an item
        """
        print("inside get_item")
        print("item given is " + item.name)
        print("counting similar items")

        carried = 0
        for i in self.inventory.values():
            if i.name == item.name:
                carried += 1
        print("already carried = ", carried)

        if item.name in self.inventory.keys():
            self.inventory[item.name + str((carried + 1))] = item
            print(item.name + " taken.")
        else:
            self.inventory[item.name] = item
            print(item.name + " taken.")

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

    def equip(self):
        print("Which item do you want to equip?")
        for i in self.inventory.values():
            print(i.name)
        choice = input()
        if choice in self.inventory.keys():
            item_to_equip = self.inventory[choice]
        if any(item_to_equip.equip_slots.values() == True):
            print("Equip where?")

            print(item_to_equip.equip_slots.keys())
            choice2 = input()

#TODO: verify that item can be equipped in selected slot, then "equip" it.
#            if item_to_equip.

    def add_xp(self, xp):
        #Generates a series of 28 multipliers to be used when calculating xp
        #gained.
        xp_multipliers = np.linspace(1.0,0.5,num=28)
        print(self.name + " had " + str(self.currentXP) + "xp.")
        x = config.char_race_xp_rate[self.race][self.char_class]
        print("Your xp multiplier is: " + str(xp_multipliers[x - 1]))
        self.currentXP += int((xp * xp_multipliers[x - 1]))
        print(self.name + " now has " + str(self.currentXP) + " xp.")

    def level_up(self):
        xp_to_lvl_up = char_level_xp_req[self.currentLevel + 1]
        if self.currentXP >= xp_to_lvl_up:
            print(self.name + " current level is: " + str(self.currentLevel))
            self.currentLevel += 1
            self.currentXP -= xp_to_lvl_up
            self.add_maxHP()
            print(self.name + " current level is: " + str(self.currentLevel))
        else:
            print("Not enough XP to purchase the next level.")

    def roll_init(self):
        self.initiative = random.randint(1,100)

    def take_dmg(self, dmg):
        self.hitPoints -= dmg
        if self.hitPoints <= 0:
            print(self.name + " should be dead.")

    def attack(self, target):
        dmg = self.AP + 1
        target.take_dmg(dmg)
        print("I am attacking " + target.name + " for " + str(dmg) +
              " points of damage.")

