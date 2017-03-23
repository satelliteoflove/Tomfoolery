worldCharacters = []

WORLD_CONFIG = {
    "dungeon_count": 1,
    "level_count":1,
    "level_width":4,
    "level_height":4
}

WALL_TYPES = {
    "clear":{"name":"clear",
             "visible":False,
             "passable":True,
             "opaque":False,
             "closed":False,
             "description":"",
             "coloring":"black"
    },
    "solid":{"name":"solid wall",
             "visible":True,
             "passable":False,
             "opaque":True,
             "closed":False,
             "description":"",
             "coloring":"white"
    }
}
