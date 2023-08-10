from kivy.lang import Builder
from kivy.uix.button import Button

Builder.load_string("""
<RoundedButton@Button>:
    background_color: (0,0,0,0)
    background_normal: ''
    canvas.before:
        Color:
            rgba: 68/255.0, 158/255.0, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [30]
""")

class RoundedButton(Button):
    pass
