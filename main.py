from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.splash import Splash
from screens.onboarding import Onboarding
from screens.login import LoginScreen


class MovieApp(App):
    def build(self):
        screen_manager = ScreenManager()
        
        screen_manager.add_widget(Onboarding(name='onboarding'))
        screen_manager.add_widget(LoginScreen(name='login'))
        screen_manager.add_widget(Splash(name='splash'))
    
        return screen_manager

if __name__ == '__main__':
    MovieApp().run()
