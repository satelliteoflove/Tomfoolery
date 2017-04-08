Level Generation
----------------
A level contains the following:
* a grid of Tile objects laid out in (x, y) dimensions
* a list of mobs which can possibly be encountered
* a maximum monster group weight
* a list of traps which may be encountered on that level

How does the level build a list of available mobs from the master list for the
dungeon?
* during creation dungeon will pass master list to new level as parameter.
* dungeon will pass minimum and maximum mob weights to new level
* level creates internal list of all mobs within min and max weights

Total mob group weight formula:




