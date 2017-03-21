In-Town resources

Bank
----
    The "Bank" is an in-town shop which allows the player to store items and
    gold outside of a character's inventory.
    The bank will not store anything for the player initially. The player will
    purchase an initial set of slots, and will need to purchase more slots as
    required.
    Unlike gold in the characters' inventories, gold in the bank will not be
    "weightless" but will "stack" and require a slot to be stored in.
    Slots can be purchased in batches of 5 for 5k gold and hold 5k gold/slot.
    Each item will take one slot.

Tavern/Pub
----------
* Add/remove character from active party
* Divvy total party gold among party members
* Accept new quests

Quests
------
Quests are occasionally picked up in the dungeon (maybe).  However, the primary
method for acquiring quests is by accepting the ones listed on the quest/bounty
board at the pub in town.  Quests are an optional way to earn more experience
and greater rewards than "grinding" alone.

Inn
---
Where characters recover hp/magic and gain levels. There is a tiered room value
structure.  At the lowest tier, the "stay" is free and the character only
regains MP. At higher (and more expensive) tiers, increasing amounts of HP are
also recovered.

Gaining levels:
    * Once necessary XP is reached by a character, they can "level up" by
      "caching in" the required XP to "purchase" the next level. Any additional
      XP will remain. Basically a special currency for character development.
    * Levels grant a random selection of stat changes
    * 1-6 stats will increase/decrease and hp will be gained based on VIT
    * Stats decrease rarely (small chance)
    * Increase/decrease happens in single increments

Market
------
Item management:
    Buy basic items/equipment
    Sell items/equipment
    Identify unknown items
    Remove cursed items that have been equipped

Temple
------
(See design doc for more on death)
Manage status ailments:
    * Cure characters of status effects for a fee (status ranking based)
    * Ressurect characters for a fee (level- and condition-based)
        * If a char is "dead", the ressurection fee is (level * 150)gold
        * If a char is "ashes" (failed ressurection), the fee
        is (level * 200)gold
"gone" characters drop their equipment in the Temple, and this equipment is
stored at the temple until retrieved by an active party.  The first chraracter
with available inventory space will receive items until their inventory is full,
then the next character with available space will receive remaining items. This
continues until all items cached at the temple are in the possession of party
characters.

Training Grounds
----------------
Character management:
    Create
    Delete/destroy
    Change name
    Change class
    
