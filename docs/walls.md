Walls
-----
Each Tile has four "walls", which can be in one of the following states. State
implies "no color" unless specifically noted.

| name         | visible | passable | opaque | closed |
|--------------|---------|----------|--------|--------|
| no wall      | F       | T        | F      | F      |
| solid wall   | T       | F        | T      | F      |
| closed door  | T       | F        | T      | T      |
| open door    | T       | T        | F      | F      |
| hidden door  | F       | F        | T      | T      |
| closed grate | T       | F        | F      | T      |
| open grate   | T       | T        | F      | F      |
| decorated    | T       | F        | T      | F      |
|--------------|---------|----------|--------|--------|

Visible: The object is visible to the player characters.

Passable: Can be walked through.

Opaque: Cannot be seen through. Generic description/note.

Closed: Can be opened, either by key or by lever.

Decorated walls contain a more detailed/quest-specific description and their
representation on the map is tinted to draw attention.


