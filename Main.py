__author__ = 'Chris'

import random, pyglet

class Character(object):
    'Common base class for all PCs and NPCs.'
    def __init__(self):
        self.name = input("What is the player's name?\n")
        self.strength = 8
        self.vitality = 8
        self.hitPoints = random.randint(5,30)
        self.attack = 10
        self.bonusPoints = random.randint(5,25)
        self.defense = 1


#Create a Pyglet Window with default values.
window = pyglet.window.Window()

#Create a "Label", which apparently is just rendered text on the screen.
label = pyglet.text.Label('This is my first text.  I imagine it will wrap at least once,'
                          ' as this is a large amount of text for just a single line.',
                          font_name='Times New Roman',
                          font_size=36, x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center',multiline=True, width=500)
@window.event()
def onKeyPress(symbol, modifiers):
    print('A key was pressed.')

@window.event()
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()