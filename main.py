import dm

# Begin initialization and presentation.
the_dm = dm.Dm()


def main():
    """Main loop.

    :returns: None

    """

    while True:
        key = input()
#        for i, word in enumerate(move):
#            print(word)     # print the command that was just entered
        if key == 'q':
            break
        else:
            the_dm.parse_command(key)


main()
