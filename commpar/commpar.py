class Commpar(object):

    def parse_command(self, move):
        if move[0] == "go":
            party1.move(move[1])
        elif move[0] == "battle":
            dm1.battle()
        elif move[0] == "encounter":
            party1.monster_encounter(1,0)
        elif move[0] == "get" or move[0] == "take":
            player.get(move[1])
        elif move[0] == "inventory":
            player.show_inventory()
        elif move[0] == "equip":
            player.equip(move[1])
        elif move[0] == "drop":
            player.drop(move[1])
        elif move[0] == "look":
            player.view_surroundings()
        elif move[0] == "attack" and move[1]:
            player.attack(move[1])
        elif move[0] == "look":
            player.view_surroundings()
        elif move[0] == "status":
            player.show_stats()
        elif move[0] == "addxp":
            player.add_xp(int(move[1]))
        elif move[0] == "levelup":
            player.level_up()
        elif move[0] == "help":
            showInstructions()
            dir(player)
        elif move[0] == "bonuspoints":
            player.bonusPoints = int(move[1])
        elif move[0] == "classchange":
            player.set_class()
        else:
            print("I have no idea what you're trying to do.")
