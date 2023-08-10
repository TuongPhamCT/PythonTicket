from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from widgets.RoundedButton import RoundedButton

Builder.load_string("""
<Onboarding>:
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 11/255.0, 15/255.0, 47/255.0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Widget:  
            size_hint_y: None
            
        Image:
            source: 'assets/images/logo.png'
                
        Label:
            text: 'New Experience'
            font_size: 30
            size_hint_y: None
            height: 45
                        
        Label:
            text: 'Watch a new movie much easier than any before'
            color: 1 , 1 , 1 , 0.5
            size_hint_y: None
            height: 20
                 
        Widget:  
            size_hint_y: None
            height: 100
            
        RoundedButton:
            text: 'Get Started'
            on_press: root.manager.current = 'login'
            size_hint_x: 0.4
            size_hint_y: None
            height: 60
            pos_hint: {'center_x': 0.5,'center_y': 0.5}
            font_size: 30
            
        BoxLayout:
            orientation: 'horizontal'    
            size_hint_x: 0.27
            size_hint_y: None
            height: 50
            pos_hint: {'center_x': 0.53,'center_y': 0.5}
            
            Label:
                text: 'Already have an Account?'
                color: 1 , 1 , 1 , 0.5
                
            Button:
                text: 'Sign In'
                background_color: 0,0,0,0
                color: 68/255.0, 158/255.0, 1, 1
                border: 0,0,0,0
                #on_press: 
        Widget:
            size_hint_y: None
            height: 100
        
""")


class Onboarding(Screen):
    pass