Design and Function

Map generation:
    Maps for each dungeon are procedurally generated at the start of a new game.
    This is not frequent, as the same save game is used regardless of the party
    members chosen.  Even if all characters in play are "gone" (dead, then ash,
    then gone), the dungeon will not change and the player will generate new
    characters and a new party and goes back into the dungeon. The dungeons are
    generated/re-generated on meeting the following conditions:
    1) The player chooses to regenerate the dungeons.  This will be an option
    within town.  Upon regeneration, all dungeons will lose their "state" and
    all saved progress and auto-maps are reset.  Any characters which are still
    in the dungeon will be returned to town and will be staying at the inn. The
    player may regenerate dungeon as many times as desired, but the prior 
    dungeon is permanently removed (no retrieval).
    2) The player chooses a "new game" from the main screen.  This will
    completely regenerate the dungeons and will permanently reset the game
    state, removing all player-generated characters, loot and progress. The
    player will be notified sufficiently of this.
    3) The player chooses to "add dungeon". This generates a brand new
    multi-level dungeon and adds it as an explorable option in the town menu.

    Generated maps are not completely random, but are generated procedurally.
    This provides the players with predictable, interesting maps and limitless
    replayability.

    Each dungeon will be a self-contained entity with 9 levels.
    Each level will be a 30x30 grid of "tiles".
    Each tile has four faces (N,S,E,W) and each one of these faces can be a
    wall, a door, or open.
    The levels will be connected by stairs (one level) and elevators
    (multi-level).
    Walls have no "thickness" but are simply barriers to passage.

Items
-----

Item drops:
    a. Item drops will be level-based, rather than monster-based.  Thus, each
    level of each tower will have a static drop list and all mobs on that
    level have the potential to drop items from that list.
    b. ALL items will be "unidentified" upon pickup. Items can be identified
    either by a character with the Bishop class or by the merchant in town.
Item properties:
    Description - Long description (if you investigate the item)
    Name - Long name (if you investigate the item)
    Short_name - Displayed in the character's inventory listing
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
        * What spell/effect(s) does it have (all derived from effect dict)
        * Weight
        * Break chance - items which have an effect when used do not have a set
          number of uses, but a chance of breaking (as a percentage) when used.
          Thus, potions, keys and scrolls have a break chance of 100%, equipment
          ranges from 0-100%, and items with no effects which can be triggered
          have a break chance of 0%.
        * Does the item remove itself from inventory after breaking, or leave a
          "broken" item in its place

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

Dealing Damage
--------------
Damage dealt is based on the following modifiers:
* Unit's base AP
* Equipment dmg/stat bonuses/modifiers
    * Strength ("adds +1 to STR")
    * baseAP ("1.2x AP")
    * direct dmg bonus ("+10dmg per hit")
    * secondary dmg bonus ("+5 fire damage")

Saving the game
---------------
Saving the game should mitigate "save scumming" (the use of frequent saves
to circumvent challenges or cheat random rolls), but should be useful to
the user.
The game should automatically save the progress of the game for the player
at regular intervals:
* After a battle concludes (win, lose or retreat)
* Upon returning to/leaving town
* Game is closed/quit
The player can save the game manually in a SEPARATE slot from the auto-save 
feature. There is only ONE slot for manual saves. When the player saves the
game again, the existing save is overwritten. The player will be allowed to
save at the following times:
* In camp
* In town
* Between battles (not during) so long as an event is not taking place

This save behavior is different in "hardcore" mode. See "hardcore mode" section.

Hardcore Mode
-------------

In hardcore mode, a number of changes make the game more challenging.

Saving:
* The player-controlled manual save game is disabled
* Automatic saving does NOT occur after battles
* The game is saved when the party returns to town
* The game is saved when the player quits the game

Mapping:
* The auto-generated map is no longer available at will - something will limit
  its use (uses a spell slot to view map or similar). The idea is to
  encourage/force the player to maintain hand-drawn maps of the dungeon. Perhaps
  the best idea is an item carried in the inventory which has a limited number
  of "charges" which are replenished upon return to town. This would work well
  in normal mode (remove the charge restriction) and hardcore mode.
  Alternately, there could be a special skill given to a specific class (such as
  mages) which allows map viewing, and charges could be applied to that skill.

Death
-----
"Death" is a vital game mechanic/aesthetic.  It should be common enough that the
player fears it but not so frequent that the game seems unfair or unplayable.
Death is a threat to all player characters - no-one is immune.
When a player character is reduced to 0 or fewer HP, that character "dies". The
character will remain in the current party until the party returns to town.
Upon the party's return to town, all "dead" or "ashes" characters will be
transferred to the Temple automatically.
The player can attempt to revive a character a limited number of times. If the
first revival fails, the character turns to "ashes".  If another revival is
attempted while the character is "ashes" and this also fails, the character is
lost forever ("gone") and they will be listed in the "hall of adventurers".
Equipment from "gone" characters will be stored at the Temple until retrieved by
the player.
(see temple in town.txt)

Monsters
--------
See "monsters.txt" 


Spells/Spellcasting
-------------------
Spells in Wizardry have classically had a unique "Wizardry" naming scheme.
Instead of "Heal" the spell is named "Dios".  Instead of "Heal more" the
spell is named "Dial".  Intstead of "Great heal" the spell is named "Dialma".
While this does give the spells a consistent naming scheme, selecting spells
is hampered by being reqired to memorize odd names or reference a list. While
this form of play should be an option, the player will also be provided with
the option to play with "Anglicised" names instead to make spell
identification easier and faster.

Slots vs. Magic Points
----------------------
Wizardry has typically employed a "spell slot" mechanic for casters. For
instance, 5/4/3/2/1/0/0/0/0 would indicate that the character could cast 5
level 1 spells, 4 level 2 spells, 3 level 3 spells, and so on. When a character
casts a spell of a given level, the number in that "slot" is decremented by
one. This is opposed to the "magic point" mechanic, where each spell has a given
cost in magic points, and the character has a "pool" of MP to draw from. It
seems that the "slot" mechanic is employed for at least two reasons: to keep
casters from being too powerful/flexible (can't cast 3 lvl 4 spells instead of
7 lvl 1 spells, etc.), and to force players to carefully manage their spells
(do I cast a damage spell in battle, or save the slot for the auto-map
feature/wall detection?). For now, I plan to keep with the "spell slot"
mechanic.

TODO:
How do event driven encounters work?
