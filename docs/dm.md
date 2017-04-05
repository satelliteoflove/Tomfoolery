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
* Party movement? (at least made aware by Party class)
* Query/pass dungeon
* Game State (Save/load/Modify/Delete)

Monster Encounters
------------------
Probability:
The DM keeps an encounter probability counter which is incremented based on
unique player group moves and decremented or cleared by level transition, spell,
or random monster encounter.

Creation steps:
* dm creates empty mob group
* dm queries current level for maximum possible mob group weight
* dm sets mob group's max weight to 1.0-0.25 x current level's max group weight
* dm queries current level for a mob type from the level's list
* dm instantiates 1-9 candidate mobs all of type x and level y for a single row
* dm queries mob group for current group weight
* if the group has room, dm adds the candidate row
* if the candidate row's collective weight is too great, dm creates a new row of
  candidates and tries again
* once the group's max weight has been reached or the dm has tried x number of
  unsuccessful candidate rows, the dm stops adding rows
* dm queries mob group if it is friendly
* if yes, dm queries player for choice (attack/wait/flee)
* if no, or if player attacks, dm queries player and mob groups for initiative
  and combat begins

Game State
----------
The dm is responsible for setting up, maintaining and saving/loading the game
state.  All game assets and interactions flow through the dm.
