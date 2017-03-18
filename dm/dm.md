What is the DM?
---------------
The "Dungeon Master" is a storyteller and referee.  Triggered events, encounters
and combat are all handled by the DM.

Triggers/Events
---------------
Event trigger statuses are requested by the DM. State is returned to DM as an
ordered list.

Triggers:
* Occupying a tile 
  * with or without "float" in effect
  * facing a specific direction
  * having an item in possession/equipped
  * chance for encounter
* Switch/lever toggled

Events/values:
* Display of clue(s) to a puzzle.
* Door/grate opening/discovery
* Flip/rotate one-way tiles
* Monster encounter
  * friendly/aggressive
    * alignment adjustment
  * party awareness/selection
  * damage transmission
  * retreat of monsters/character party
* Party movement
* Query/pass dungeon
* Game State (Save/load/Modify/Delete)
