from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image


Builder.load_string("""
<Splash>:
    BoxLayout:
        canvas.before:
            Color:
                rgba: 11/255.0, 15/255.0, 47/255.0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Image:
            source: 'assets/images/logo.png'
""")

class Splash(Screen):
    pass
