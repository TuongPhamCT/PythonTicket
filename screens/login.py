from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from widgets.RoundedButton import RoundedButton

Builder.load_string("""
<LoginScreen>:
    BoxLayout:
        orientation: 'horizontal'
        canvas.before:
            Color:
                rgba: 11/255.0, 15/255.0, 47/255.0, 1
            Rectangle:
                pos: self.pos
                size: self.size
                
        BoxLayout:
            orientation: 'vertical'   
            
            Widget:  
                size_hint_y: None
                height: 210     
                
            Image:
                source: 'assets/images/logo.png'
                
            Label:
                text: 'Welcome back, Movie Lover!'
                font_size: 30
                
            Widget:  
                size_hint_y: None
                height: 300
            
        BoxLayout:
            orientation: 'vertical'
            
            Widget:  
                size_hint_y: None
                height: 150  
                
            TextInput:
                id: username_input
                hint_text: 'Email address'
                multiline: False
                size_hint_x: 0.8
                size_hint_y: None
                height: 50
                pos_hint: {'center_x': 0.5,'center_y': 1}
                font_size: 23
            
            Widget:  
                size_hint_y: None
                height: 10
                
            TextInput:
                id: password_input
                hint_text: 'Password'
                multiline: False
                password: True
                size_hint_x: 0.8
                size_hint_y: None
                height: 50
                pos_hint: {'center_x': 0.5,'center_y': 1}
                font_size: 23
            
            Button:
                text: 'Forgot Password?'
                background_color: 0,0,0,0
                color: 1,1,1,1
                border: 0,0,0,0
                on_press: root.manager.current = 'login'
                font_size: 18
                pos_hint: {'center_x': 0.75,'center_y': 1}
                size_hint_y: None
                height: 30
                    
            Widget:  
                size_hint_y: None
                height: 50   
                 
            RoundedButton:
                text: 'Login'
                on_press: root.login()
                size_hint_x: 0.7
                size_hint_y: None
                height: 60
                pos_hint: {'center_x': 0.5,'center_y': 0.5}
                font_size: 30
                
            BoxLayout:
                orientation: 'horizontal'    
                size_hint_x: 0.48
                pos_hint: {'center_x': 0.53,'center_y': 0.5}
                
                Label:
                    text: 'Create new account?'
                    color: 1 , 1 , 1 , 0.5
                    
                Button:
                    text: 'Sign Up'
                    background_color: 0,0,0,0
                    color: 68/255.0, 158/255.0, 1, 1
                    #on_press:
                    
            BoxLayout:
                orientation: 'horizontal'
                size_hint_x: 0.4
                pos_hint: {'center_x': 0.5,'center_y': 1}
                
                Image:
                    source: 'assets/images/media_google.png'
                
                Image:
                    source: 'assets/images/media_facebook.png'
            
            Widget:
                size_hint_y: None
                height: 60
""")


class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text
        password = self.ids.password_input.text
        if(username=='admin' and password == 'admin'):
            self.manager.current = 'home'
