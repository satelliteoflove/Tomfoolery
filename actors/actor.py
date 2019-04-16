#!/usr/bin/env python3

from numpy import random, linspace


class Actor(object):
    """Common base class for all PCs and NPCs."""

    def __init__(self):
        self._name = ""
        self._current_level = 0
        self._current_xp = 0
        self._agility = 0
        self._intelligence = 0
        self._luck = 0
        self._piety = 0
        self._strength = 0
        self._vitality = 0
        self._inventory = {}

#    def __init__(self, class_config, race_config):
#        """Creates a playable character."""
#        #self._name = self.set_name()
#        #self._current_level = 1
#        #self._current_xp = 0
#        # _stat_names is only used in a helper function to determine if a named
#        # stat is legitimate. This will likely be unnecessary after input is
#        # driven by something other than the command interpreter.
#        self._stat_names = ["strength", "agility", "vitality", "intelligence",
#                            "piety", "luck"]
#        #self._strength = 0
#        #self._agility = 0
#        #self._vitality = 0
#        #self._intelligence = 0
#        #self._piety = 0
#        #self._luck = 0
#        self._race = self.set_race(race_config)
#        self.set_sex()
#        self.set_bonusPoints()
#        self.set_class(class_config)
#        self.assign_BonusPoints()
#        self.set_xp_rate()
#        self.set_initial_HP()
#        self.set_class_AC()  # As in characters.md - AD&D rules for AC/THAC0.
#        self.set_THAC0()
#        #self._inventory = {}
#        self.equipment = {"head": 0, "body": 0, "legs": 0, "arms": 0,
#                          "hands": 0, "feet": 0, "accessory": 0, "lhand": 0,
#                          "rhand": 0}
#        self.set_AP()
#        self.action_list = {}
#        self.type = False
#        self.position = None

    def show_inventory(self):
        # list items, none if empty
        if len(self._inventory) > 0:
            for k in self._inventory.keys():
                print(k)
        else:
            print("You aren't carrying anything.")

    def set_class_AC(self):
        """Set character's class-based AC "base"."""
        self.AC = config[self.char_class]["AC"]

    def set_THAC0(self):
        """Set character's class-based THAC0 "base"."""
        self.THAC0 = 20 - round((self._current_level *
            config[self.char_class]["THAC0mult"]))

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
        chance = random.randint(0, 1)

        if self.char_class == "samurai":
            if chance == 0:
                self.hitPoints = int(16 + self._vitality // 2)
            if chance == 1:
                self.hitPoints = (9 * (16 + self._vitality // 2) // 10)
        elif self.char_class == "fighter" or self.char_class == "lord":
            if chance == 0:
                self.hitPoints = 10 + self._vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (10 + self._vitality // 2) // 10)
        elif self.char_class == "priest":
            if chance == 0:
                self.hitPoints = 8 + self._vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (8 + self._vitality // 2) // 10)
        elif self.char_class == "thief" or self.char_class == "ninja":
            if chance == 0:
                self.hitPoints = 6 + self._vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self._vitality // 2) // 10)
        elif self.char_class == "bishop":
            if chance == 0:
                self.hitPoints = 6 + self._vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (6 + self._vitality // 2) // 10)
        elif self.char_class == "mage":
            if chance == 0:
                self.hitPoints = 4 + self._vitality // 2
            if chance == 1:
                self.hitPoints = (9 * (4 + self._vitality // 2) // 10)

        if self.hitPoints < 2:
            self.hitPoints = 2

        self.maxHitPoints = self.hitPoints

    def add_maxHP(self):
        """Adds max HP when character gains a level.

        TODO: Ensure that vitality modifies added maximum HP.
        """
        if self.char_class == "fighter" or self.char_class == "lord":
            self.maxHitPoints += int(random.triangular(0, 10, 5))
        elif self.char_class == "priest" or self.char_class == "samurai":
            self.maxHitPoints += int(random.triangular(0, 8, 4))
        elif self.char_class == "monk":
            self.maxHitPoints += int(random.triangular(0, 8, 5))
        elif self.char_class == "thief" or self.char_class == "ninja":
            self.maxHitPoints += int(random.triangular(0, 6, 3))
        elif self.char_class == "bishop":
            self.maxHitPoints += int(random.triangular(0, 6, 3))
        elif self.char_class == "mage":
            self.maxHitPoints += int(random.triangular(0, 4, 2))

    def set_sex(self):
        """Sets the sex of the character.

        The sex of a character grants a one-time stat bonus upon character
        creation (+1 VIT (F)/+1 STR (M)), and only women can be valkyries.
        """
        # Quick hack
        self.sex = "male"

        # self.sex = ""
        while self.sex != "male" and self.sex != "female":
            print("What is the sex of the character?\n(male or female)")
            self.sex = input().lower()
        if self.sex == "male":
            self._strength += 1
        elif self.sex == "female":
            self._vitality += 1

    def set_bonusPoints(self):
        """Assigns starting bonus points.
        """
        self.bonusPoints = 0
        while self.bonusPoints < 4:
            self.bonusPoints = int(random.normal(8, 4))
        print("Bonus Points = " + str(self.bonusPoints))

    def set_race(self, config):
        """Used on character creation to set race values.

        After choosing a race, the minimum stat values are set for the
        character based on racial minimums.  In addition, any special fields
        such as resistance values or special attacks are set.

        :config: dictionary of available races and their attributes
        """
        print("What race is this character?\n")
        for key in config.keys():
            print(key)

        self._race = None
        while self._race is None:
            tryrace = input().lower()
            if tryrace in config.keys():
                return tryrace
            else:
                print("That is not a valid race.")
                print("What race is this character?\n")
                for key in config.keys():
                    print(key)
        self._strength = config[self._race]["min_str"]
        self._vitality = config[self._race]["min_vit"]
        self._agility = config[self._race]["min_agi"]
        self._intelligence = config[self._race]["min_int"]
        self._piety = config[self._race]["min_pie"]
        self._luck = config[self._race]["min_luk"]

    def set_name(self):
        name_accepted = False
        while name_accepted is False:
            try_name = input("What is the player's name?\n")
            if len(try_name) > 12:
                print("Name is too long. Must be 12 characters or less.")
            else:
                name_accepted = True
        return try_name

    def validate_class(self, class_config, newclass):
        """Validates that a class can be chosen for the character by comparing
        total bonus points required vs current bonus points.
        """
        config = class_config
        points_required = 0
        str_req = config[newclass]["min_str"]
        agi_req = config[newclass]["min_agi"]
        vit_req = config[newclass]["min_vit"]
        int_req = config[newclass]["min_int"]
        pie_req = config[newclass]["min_pie"]
        luk_req = config[newclass]["min_luk"]

        if str_req > self._strength:
            points_required += str_req - self._strength
        if agi_req > self._agility:
            points_required += agi_req - self._agility
        if vit_req > self._vitality:
            points_required += vit_req - self._vitality
        if pie_req > self._piety:
            points_required += pie_req - self._piety
        if luk_req > self._luck:
            points_required += luk_req - self._luck

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

    def set_class(self, config):
        """Modifications specific to class changes.

        Includes statistic changes, class variable update, etc.
        In addition, the rate of HP growth is defined here.
        """
        classlist = []
        for classname in config.keys():
            if self.validate_class(config, classname):
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
                str_req = config[try_class]["min_str"]
                agi_req = config[try_class]["min_agi"]
                vit_req = config[try_class]["min_vit"]
                int_req = config[try_class]["min_int"]
                pie_req = config[try_class]["min_pie"]
                luk_req = config[try_class]["min_luk"]

                if str_req > self._strength:
                    self.bonusPoints -= str_req - self._strength
                    self._strength = str_req
                if agi_req > self._agility:
                    self.bonusPoints -= agi_req - self._agility
                    self._agility = agi_req
                if vit_req > self._vitality:
                    self.bonusPoints -= vit_req - self._vitality
                    self._vitality = vit_req
                if pie_req > self._piety:
                    self.bonusPoints -= pie_req - self._piety
                    self._piety = pie_req
                if luk_req > self._luck:
                    self.bonusPoints -= luk_req - self._luck
                    self._luck = luk_req

    def assign_BonusPoints(self):
        """Assigns attribute points during character creation."""
        # Save this for later
        initial_bonuspoints = self.bonusPoints

        print("There are " + str(self.bonusPoints) + " remaining bonus points.")
        print("Your current statistics are: ")
        print("[S]trength: " + str(self._strength))
        print("[A]gility: " + str(self._agility))
        print("[V]itality: " + str(self._vitality))
        print("[I]ntelligence: " + str(self._intelligence))
        print("[P]iety: " + str(self._piety))
        print("[L]uck: " + str(self._luck))
        while self.bonusPoints > 0:
#            stat_increased = 's'
            stat_increased = input().lower()
            if stat_increased == 's':
                stat_increased = "_strength"
            elif stat_increased == 'a':
                stat_increased = "_agility"
            elif stat_increased == 'v':
                stat_increased = "_vitality"
            elif stat_increased == 'i':
                stat_increased = "_intelligence"
            elif stat_increased == 'p':
                stat_increased = "_piety"
            elif stat_increased == 'l':
                stat_increased = "_luck"

            if stat_increased not in self._stat_names:
                print("That isn't a stat. Try again.")
            else:
                setattr(self, stat_increased, getattr(self, stat_increased) + 1)
                self.bonusPoints -= 1
                print("Bonus Points = " + str(self.bonusPoints))
                print("Strength: " + str(self._strength))
                print("Agility: " + str(self._agility))
                print("Vitality: " + str(self._vitality))
                print("Intelligence: " + str(self._intelligence))
                print("Piety: " + str(self._piety))
                print("Luck: " + str(self._luck))
        print("You don't have any bonus points left.")

    def set_xp_rate(self):
        """Sets the experience multiplier for a given race/class combination.
        """
        print("Setting xp rate multiplier.")
        print("self.char_class = " + self.char_class)
        print("self._race = " + self._race)
        print("My 'rate' is: " + str(
                            config.char_race_xp_rate[self._race][self.char_class]))
        if self._race in config.char_race_xp_rate:
            if self.char_class in config.char_race_xp_rate[self._race]:
                self.rate = config.char_race_xp_rate[self._race][self.char_class]
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
        if self._strength == 3:
            self.AP -= 3
        if self._strength == 4:
            self.AP -= 2
        if self._strength == 5:
            self.AP -= 1
        if self._strength > 15:
            self.AP += 1 * (self._strength - 15)
        if self.AP < 0:
            self.AP = 0
        print("This character's AP is: " + str(self.AP))

    def return_stats(self):
        """Used to view full, raw information about a specific character."""
        return collections.OrderedDict(vars(self))

    def get_item(self, item):
        """PC gets an item.
        """
        print("inside get_item")
        print("item given is " + item.name)
        print("counting similar items")

        carried = 0
        for i in self._inventory.values():
            if i.name == item.name:
                carried += 1
        print("already carried = ", carried)

        if item.name in self._inventory.keys():
            self._inventory[item.name + str((carried + 1))] = item
            print(item.name + " taken.")
        else:
            self._inventory[item.name] = item
            print(item.name + " taken.")

    def drop(self, item_to_drop):
        pass

    def equip(self):
        """Equip the character with an item from that character's inventory."""
        #TODO: Currently, no checks are made for equipping one item in multiple
        #slots, or for over-writing what is equipped in a slot. To replicate, give
        #character two items and try to equip them.
        print("Which item do you want to equip?")
        for i in self._inventory.keys():
            print(i)
        choice = input()
        if choice in self._inventory.keys():
            if self._inventory[choice].is_equipped == False:
                item_to_equip = self._inventory[choice]
            else:
                print("That item is already equipped.")
                self.equip()
        if any(item_to_equip.equip_slots.values()):
            print("Equip where?")
            for k, v in item_to_equip.equip_slots.items():
                if v == True:
                    print(k)
            choice2 = input()
            self.equipment[choice2] = item_to_equip
            self._inventory[choice].is_equipped = True

    def new_equip(self):
        """Equip items from inventory."""
        # first, enumerate equipment slots
        # for each slot, determine which items from inventory can be equipped.
        # list those items and allow player to select.
        # for each selection, allow an item or "none".
        print("The following items are equipped:")
        slot_listing = self.equipment.keys()
        print(dict(enumerate(slot_listing)))
        print("Please choose a slot to equip, or choose 'None'.")
        #for slot, value in self.equipment.items():
        #    print(slot)
        #    if value == 0:
        #        print("Currently equipped: Empty")
        #    else:
        #        print("Currently equipped: " + value.name)
        #    print("The following items can be equipped here:")
        #    print(enumerate(self.inventory.values()))
        #    for item in self.inventory.values():
        #        print(item.name)
            
        pass

    def add_xp(self, xp):
        # Generates a series of 28 multipliers to be used when calculating xp
        # gained.
        xp_multipliers = linspace(1.0, 0.5, num=28)
        print(self.name + " had " + str(self._current_xp) + "xp.")
        x = config.char_race_xp_rate[self._race][self.char_class]
        print("Your xp multiplier is: " + str(xp_multipliers[x - 1]))
        self._current_xp += int((xp * xp_multipliers[x - 1]))
        print(self.name + " now has " + str(self._current_xp) + " xp.")

    def level_up(self):
        xp_to_lvl_up = char_level_xp_req[self._current_level + 1]
        if self._current_xp >= xp_to_lvl_up:
            print(self.name + " current level is: " + str(self._current_level))
            self._current_level += 1
            self._current_xp -= xp_to_lvl_up
            self.add_maxHP()
            print(self.name + " current level is: " + str(self._current_level))
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


class Mob(Actor):
    def __init__(self, mob_list, type_name, level):
        self.type_name = mob_list[type_name]["typename"]
        self.type = mob_list[type_name]["type"]
        self.name = self.type_name
        self.level = level
        self._agility = mob_list[type_name]["agility"]
        self.HP = mob_list[type_name]["base_hp"] * self.level
        self.THAC0 = mob_list[type_name]["THAC0"]
        self.AP = mob_list[type_name]["base_ap"] * self.level // 2
        self.weight = round(mob_list[type_name]["party_weight"] * self.level, 1)
        self.weapon_slots = mob_list[type_name]["wslots"]
        self.attacks = mob_list[type_name]["attacks"]
        self.alignment = mob_list[type_name]["alignment"]
        if self.AP < 1:
            self.AP = 1
#        self.show_stats()

    def roll_init(self):
        self.initiative = random.randint(1,100)

    def show_stats(self):
        print("Stats of monster '%s':" %self.name)
        print(vars(self))

    def take_dmg(self, damage):
        self.HP -= damage
        print("I, " + self.name + ", took " + str(damage) + " damage.")

    def attack(self, target):
        dmg = self.AP + 1
        target.take_dmg(dmg)
        print("I am attacking " + target.name + " for " + str(dmg) +
              " points of damage.")
