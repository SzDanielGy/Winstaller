import os
cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + "/conf"
fontswd = f'{cwd}\conf\data\\fonts'
from kivy.config import Config
Config.set("graphics","width","1024")
Config.set("graphics","height","768")
Config.set("kivy", "default_font", [fontswd+"\\times.ttf",fontswd+"\\timesi.ttf",fontswd+"\\timesbd.ttf",fontswd+"\\timesbi.ttf"])
Config.set('graphics', 'fullscreen', '0')
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty
from lang import Lang
from m_screen import M_screen

Lang()

M_screen()
 
class QnA(Screen):
   pass

class Manager(ScreenManager):
    pass

kv = Builder.load_file("lib/kv/main.kv")

class MainApp(App):
    def build(self):
        return kv
    
if __name__ == "__main__":
    MainApp().run()
    