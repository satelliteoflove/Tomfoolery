import dm
import curses

# Begin initialization and presentation.
the_dm = dm.Dm()

def main():
    """Main loop.

    Returns:
        None
    """

    while True:
        move = input(">").lower().split()
        for i, word in enumerate(move):
            print(word)     # print the command that was just entered
        if move[0] == 'q' or move[0] == "quit":
            break
        else:
            the_dm.parse_command(move)

main()
