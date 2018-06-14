from fabulous.color import fg256, bg256, bold, magenta, highlight_red
from fabulous import utils
from fabulous import image
from fabulous import text

print(fg256('#F0F', 'hello world'))

print(fg256('magenta', 'hello world'))

print(text.Text("You are win!", color='#0099ff', shadow=True, skew=5))

print(image.Image("wizardry1-ibm-2.png"))
