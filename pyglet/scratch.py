import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label("Yo this is some text.",
                          font_name="Courier",
                          font_size=28,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    label.draw()

music = pyglet.resource.media()

window.push_handlers(pyglet.window.event.WindowEventLogger())

pyglet.app.run()