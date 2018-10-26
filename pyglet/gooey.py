import pyglet
import glooey

class MyLabel(glooey.Label):
    custom_color = '#babdb6'
    custom_font_size = 10
    custom_alignment = 'center'

class MyTitle(glooey.Label):
    custom_color = '#eeeeec'
    custom_font_size = 12
    custom_alignment = 'center'
    custom_bold = True

class MyButton(glooey.Button):
    Label = MyLabel
    custom_alignment = 'fill'

    class Base(glooey.Background):
        custom_color = '#204a87'

    class Over(glooey.Background):
        custom_color = '#3465a4'

    class Down(glooey.Background):
        custom_color = '#729fcff'

    def __init__(self, text, response):
        super().__init__(text)
        self.response = response

    def on_click(self, widget):
        print(self.response)

window = pyglet.window.Window()
gui = glooey.Gui(window)

vbox = glooey.VBox()
vbox.alignment = 'top left'

title = MyTitle("Look at me now!")
vbox.add(title)

buttons = [
    MyButton("Blue", "Right, off you go"),
    MyButton("Blue. No yel---", "Auuuuuuugh!"),
    MyButton("I don't know that!", "Auuuuuuugh!")
]

for button in buttons:
    vbox.add(button)

gui.add(vbox)

pyglet.app.run()