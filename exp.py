
ATTRIBUTES = {
    'strength': 1,
    'intelligence': 1,
    'wisdom': 1,
    'charisma': 1,
    'constitution': 1,
    'dexterity': 1
}

CLASS_MODIFIERS = {
    'warrior': {
        'strength': 1.1,
        'intelligence': 0.9,
        'wisdom': 0.9,
        'charisma': 1.1,
        'constitution': 1.5,
        'dexterity': 0.8
    },
    'mage': {
        'strength': 0.8,
        'intelligence': 1.3,
        'wisdom': 1.1,
        'charisma': 0.9,
        'constitution': 0.8,
        'dexterity': 1.2
    },
    'cleric': {
        'strength': 0.9,
        'intelligence': 1.1,
        'wisdom': 1.3,
        'charisma': 1,
        'constitution': 1.1,
        'dexterity': 1.4
    }
}

RACE_MODIFIERS = {
    'human': {
        'strength': 1.1,
        'intelligence': 0.9,
        'wisdom': 0.9,
        'charisma': 1.1,
        'constitution': 1,
        'dexterity': 1
    },
    'elf': {
        'strength': 0.8,
        'intelligence': 1.1,
        'wisdom': 1.1,
        'charisma': 1.2,
        'constitution': 1.2,
        'dexterity': 1.2
    },
    'dwarf': {
        'strength': 1.2,
        'intelligence': 0.9,
        'wisdom': 0.9,
        'charisma': 0.8,
        'constitution': 1.2,
        'dexterity': 0.8
    }
}

class CharacterClass(object):
    def __init__(self, name, strength=1, intelligence=1, wisdom=1, charisma=1,
        constitution=1, dexterity=1):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.constitution = constitution
        self.dexterity = dexterity
        self.experience = 0
        self.level = 0

    def add_experience(self, exp):
        self.experience += (exp * self.intelligence)

    def __str__(self):
        return (
            'name: {:<14} '.format(self.name) +
            'str: {:<5} int: {:<5} wis: {:<5} chr: {:<5} con: {:<5} dex: {:<5}'.format(
                self.strength,
                self.intelligence,
                self.wisdom,
                self.charisma,
                self.constitution,
                self.dexterity
            )
        )

def generate_character_classes():
    classes = []
    for race_name in RACE_MODIFIERS.keys():
        for class_name in CLASS_MODIFIERS.keys():
            attributes = dict(ATTRIBUTES)
            race_mod = RACE_MODIFIERS.get(race_name)
            class_mod = CLASS_MODIFIERS.get(class_name)
            name = '{} {}'.format(race_name, class_name)
            for attribute_modifiers in [race_mod, class_mod]:
                for attr, modifier in attribute_modifiers.items():
                    attributes[attr] *= modifier
            c = CharacterClass(name, **attributes)
            classes.append(c)
    return classes



if __name__ == '__main__':
    character_classes = generate_character_classes()
    for cc in character_classes:
        print cc
