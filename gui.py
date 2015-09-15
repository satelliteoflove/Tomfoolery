__author__ = 'Chris'

import tkinter, turtle, sys

def main():

    root_window = tkinter.Tk()
    root_window.title("Wizardry Clone")

    cv = tkinter.Canvas(root_window, width=600, height=600) # create a "canvas" widget within the root window
    cv.pack(side = tkinter.LEFT) # "pack" the widget to the left side of its container

    t = turtle.RawTurtle(cv)

    screen = t.getscreen()

    frame = tkinter.Frame(root_window)
    frame.pack(side = tkinter.RIGHT, fill=tkinter.BOTH)

    def quitHandler():
        sys.exit(0)

    quitButton = tkinter.Button(frame,text="quit",command=quitHandler)
    quitButton.pack()



    tkinter.mainloop()

if __name__ == "__main__":
    main()