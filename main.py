from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.SignUpScreen import SignUpScreen


class MovieApp(App):
    def build(self):
        screen_manager = ScreenManager()
        
        screen_manager.add_widget(SignUpScreen(name='signup'))
    
        return screen_manager

if __name__ == '__main__':
    MovieApp().run()