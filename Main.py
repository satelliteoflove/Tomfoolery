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
main_window = pyglet.window.Window(caption='Main Window')
message_window = pyglet.window.Window(caption='Message Window')

#label = pyglet.text.Label('This is my first text.  I imagine it will wrap at least once,'
#                          ' as this is a large amount of text for just a single line.',
#                          font_name='Times New Roman',
#                          font_size=36, x=main_window.width//2, y=main_window.height//2,
#                          anchor_x='center', anchor_y='center',multiline=True, width=500)

scrolling_text = pyglet.text.layout.ScrollableTextLayout('This is some text to scroll.  It is my hope, '
                                                         'that the pyglet functionality built in to the '
                                                         'ScrollableTextLayout thingy will not require '
                                                         'the specific use of the newline character.  But,'
                                                         ' it probably will require that and much more.  '
                                                         'Hard to say.  This however is a running paragraph that '
                                                         'might as well be Latin.',500,500)
message_label = pyglet.text.Label('This is for the message window.  This message will also'
                                  ' automatically wrap due to length, but probably in a '
                                  'different place.', font_name='Arial', font_size=18,
                                  x=message_window.width//2, y=message_window.height//2,
                                  anchor_x='center', anchor_y='center', multiline=True, width=500)

@message_window.event()
def on_draw():
    message_window.clear()
    message_label.draw()

@main_window.event()
def on_draw():

    main_window.clear()
    #label.draw()
    scrolling_text.draw()

pyglet.app.run()