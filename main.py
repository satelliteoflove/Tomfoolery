import dm
import curses

# Begin initialization and presentation.
the_dm = dm.Dm()

def main(stdscr):
    """Main loop.

    :returns: TODO

    """
    stdscr.clear()

    while True:
        stdscr.clear()
        move = stdscr.getstr(
#        move = input(">").lower().split()
    #    for i, word in enumerate(move):
    #        print(word)     # print the command that was just entered
        if move[0] == 'q' or move[0] == "quit":
            break
        else:
            the_dm.parse_command(move)
        stdscr.refresh()

curses.wrapper(main)
