from curses import wrapper
import curses
import main


def main(stdscr):
    #Clear screen
    stdscr.clear()

    #Raises error @ i == 10
    for i in range(0,11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
