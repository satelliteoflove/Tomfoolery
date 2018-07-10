Items
-----

Item drops:
    a. Item drops will be level-based, rather than monster-based.  Thus, each
    level of each tower will have a static drop list and all mobs on that
    level have the potential to drop items from that list.
    b. Some specific efents will drop specific items.
    c. All lootable items will initially be "unidentified". Items can be
    identified either by a character with the Bishop class or by the merchant
    in town.

Item properties:
    * Description - Long description.
    * Name - Item name displayed if item is identified.  "Potion of Healing"
    vs. "Potion".
    * Generic Name - Name displayed if item specifics are unknown.  I.E.,
    "sword" instead of "short sword" or "sword of ice".
    * Weight - integer value
    * Minimum/Maximum Damage
    * Slot which item can be equipped in.
    * Element (fire/water/physical, etc.)
    * Number of attacks
    * Range (front row, back row, both)
    * Scope (one mob, one mob group, one row, all mobs)


Notes:
    Once acquired, items occupy an inventory slot until they are used or
    destroyed.  Items can be deposited in town at the appropriate shop (see
    "bank" below).
    When "dropped", an item is destroyed and gone forever.
    All items can be used at any time, but only have an effect under specific
    conditions.
    Items such as potions and scrolls are single-use "portable spells" that can
    be used by any character class or race. When used, they are marked as 
    "broken" and are unusable. In classic Wizardry, there is no way to repair 
    these items - they just take up space until they are dropped (destroyed).
    Should it be possible to "repair" "broken" items if certain conditions are 
    met?

Random items:
    If item randomization were to be included:
    * Item catalog is built at the start of a new game, before dungeons.
    * Item naming and effects:
        * Item type ("potion", "short sword", "key")
        * Affix ("healing", "nimble", "gate")
        * Suffix ("fear", "flames", "silver")
        * Each item type will have basic shared characteristics
        * Thus, names such as "healing potion of fear", "nimble short sort of
          flames" and "gate key of silver" would be derived from the above.
          Affixes/suffixes are not always both present; "key of silver" and 
          "nimble potion" are perfectly acceptable item names.
        * Affixes/suffixes each have a specific effect, such as healing a
          target (heal1), opening a door or setting a target on fire(fire3).
    * What can be defined by an item type?
        * Can the item be equipped
        * How many of that type can be equipped at once
        * Weight
        * Break chance - items which have an effect when used do not have a set
          number of uses, but a chance of breaking (as a percentage) when used.
          Thus, potions, keys and scrolls have a break chance of 80-100%, 
          equipment ranges from 0-100%.  Items with no effects which can be 
          triggered have a break chance of 0%.
        * "Generic name" for unidentified items. (i.e. "blade" for long and
          short swords, daggers, etc. or "bludgeon" for clubs, maces and
          hammers.)
        * Does the item remove itself from inventory after breaking, or leave a
          "broken" item in its place
    * What can be defined by an affix/suffix?
        * One specific named effect (all derived from effect dict)
        * Affixes are generally preceding adjectives such as "brilliant" or
          "shuddering"
        * Suffixes are generally nouns or trailing verbs such as 


Equipment
---------
Weapons, Armor, Accessories are all "equipment" but are still instances of the 
"Item" class.  Equipment will have a different initialization method (__init__) 
which requires the appropriate input (listed below).

Equipment properties:
    Is_equippable(t/f)
    Is_equipped(t/f)
    Min_dmg(int)
    Max_dmg(int)
    Hit_multiplier(float)
    Equip_effect([]) - list of index numbers/keys. There will be a dictionary of
    "spell" effects, and this list contains a key for each effect the item needs
    to have when equipped.
    Use_effect(int) - key related to the spell dictionary, for what effect the
    item has when used as an item

