_How does this module function_

* DM object has current pc party and generated mob party.
* DM requests a battle grid dict from Combat, sends it pc party and mob party
  as _lists_.
* lists are used to  


* Chance for peaceful encounter
* Hostile mobs - two windows:
    * Names/stats of mobs
    * User input & combat log
* Monsters initially are only described by type
    * Mobs ID'ed after:
        * successful IQ check
        * party member previously encountered (x) times
        * LATUMAPIC spell cast
* Combat proceeds in rounds
    * All character actions are queued based on initiative
    * Each character chooses an action:
        * (F)ight - physical attack with equipped weapon - front row only
        * (P)arry - increases evasion
        * (D)ispell
* Combat ends when either side escapes or is totally defeated

