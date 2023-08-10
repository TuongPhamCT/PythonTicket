from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from widgets.RoundedButton import RoundedButton
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Ellipse, Color


Builder.load_string("""
<SignUpScreen>:
    BoxLayout:
        orientation:'vertical'
        padding: 30
        canvas.before:
            Color:
                rgba: 11/255.0, 15/255.0, 47/255.0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        BoxLayout:
            pos_hint: {'top': 1, 'left': 1}
            size_hint_x: 1
            size_hint_y: None
            size: '200dp','50dp'
            orientation: 'horizontal'
            Image:
                source: 'assets/icons/back.png'
                size_hint: None, None
                size: '30dp','30dp'
            Label:
                text: 'Create Your New Account'
                font_size: 50
            Widget:
                size_hint: None, None
                width: 40
        Widget:
            size_hint: None, None
            height: 50

        BoxLayout:
            orientation: 'vertical'
            size_hint: None, None
            size: 100, 100
            pos_hint: {'center_x': 0.5, 'center_y': 1}
            canvas:
                Color:
                    rgb: 1, 1, 1
                Ellipse:
                    pos: self.pos
                    size: 100, 100
                    source: 'assets/images/profile.png'
                    angle_start: 0
                    angle_end: 360
            Image:
                size: 30, 30
                source: 'assets/images/add.png'
                size_hint: None, None
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                
        Widget:
            size_hint: None, None
            height: 50
        TextInput:
            id: fullnameip
            hint_text: 'Full Name'
            multiline: False
            password: False
            size_hint_x: 0.7
            size_hint_y: None
            height: 50
            pos_hint: {'center_x': 0.5,'center_y': 1}
            font_size: 23
            background_color: 0.8, 0.8, 0.8, 0
            padding: 13
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 20)
        Widget:  
            size_hint_y: None
            height: 20
        TextInput:
            id: emailip
            hint_text: 'Email Address'
            multiline: False
            password: False
            size_hint_x: 0.7
            size_hint_y: None
            height: 50
            pos_hint: {'center_x': 0.5,'center_y': 1}
            font_size: 23
            background_color: 0.8, 0.8, 0.8, 0
            padding: 13
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 20)
        Widget:  
            size_hint_y: None
            height: 20
        TextInput:
            id: passwordip
            hint_text: 'Password'
            multiline: False
            password: True
            size_hint_x: 0.7
            size_hint_y: None
            height: 50
            pos_hint: {'center_x': 0.5,'center_y': 1}
            font_size: 23
            background_color: 0.8, 0.8, 0.8, 0
            padding: 13
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 20)
        Widget:  
            size_hint_y: None
            height: 20
        TextInput:
            id: confirmpassip
            hint_text: 'Confirm Password'
            multiline: False
            password: True
            size_hint_x: 0.7
            size_hint_y: None
            height: 50
            pos_hint: {'center_x': 0.5,'center_y': 1}
            font_size: 23
            background_color: 0.8, 0.8, 0.8, 0
            padding: 13
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Line:
                    rounded_rectangle: (self.x, self.y, self.width, self.height, 20)
        Widget:  
            size_hint_y: None
            height: 20
        RoundedButton:
            text: 'Sign In'
            on_press: pass
            size_hint_x: 0.4
            size_hint_y: None
            height: 60
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            font_size: 30
        Widget:  
            size_hint_y: None
            height: 50
""")


class SignUpScreen(Screen):
    def signup(self):
        pass
