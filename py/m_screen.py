import os
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.properties import BooleanProperty

d_path = ''
i_path = ''

'''if sys.platform == 'win32' and os.name == 'nt':
    if sys.getwindowsversion().major >= 6:
        try:
            os.system('runas /user:Administrator cmd.exe')
        except:
            print('A program futtatása adminisztrátori jogosultságokkal sikertelen.')
            sys.exit(0)'''

def M_screen():
    
    global d_path
    global i_path



    def import_winget():
        winget = []
        folder_names = []
        with open(i_path,"r+",encoding="utf8") as file:
            for line in file:
                winget.append(line.strip())
                lines = line.strip().split(".")
                folder_names.append(lines[-1])              
        file.close()
        for i in range(len(winget)):
            print(winget[i])
            
            os.system (f'winget install {winget[i]} -e --force --location "{d_path}\{folder_names[i]}"')
        


    
    class FolderOpen(Popup):
        def __init__(self, main_screen):
            super(FolderOpen, self).__init__()
            self.main_screen = main_screen

        def select_folder(self, path):
            # str(path)
            other_screen = self.main_screen.manager.get_screen('main')
            other_screen.ids.destination_i.text = str(path)
            global d_path
            d_path = str(path)
            """for i, widget in enumerate(other_screen.ids.items()):
                print(widget[1])"""

                
                
    class IFolderOpen(Popup):
        def __init__(self, main_screen):
            super(IFolderOpen, self).__init__()
            self.main_screen = main_screen
        
        def select_i_folder(self, path, filename):
            full_path = os.path.join(path, filename)
            other_screen = self.main_screen.manager.get_screen('main')
            other_screen.ids.input_i.text = str(full_path)
            global i_path
            i_path = str(full_path)
            #print(i_path)



    class MainScreen(Screen):
        
        def language_on(self):
            self.ids.language_b.source = "lib/images/language_pressed.png"
            
        def language_off(self):
            self.ids.language_b.source = "lib/images/language.png"     



        def qna_on(self):
            self.ids.qna_b.source = "lib/images/qna_pressed.png"
            
        def qna_off(self):
            self.ids.qna_b.source = "lib/images/qna.png"
            
            
            
        def folder_on(self):
            self.ids.destination_b.source = "lib/images/folder_pressed.png"
            
        def folder_off(self):
            self.ids.destination_b.source = "lib/images/folder.png"
        
        
        
        def i_folder_on(self):
            self.ids.input_b.source = "lib/images/folder_pressed.png"
            
        def i_folder_off(self):
            self.ids.input_b.source = "lib/images/folder.png"
        
        
        
        def text_enter_i(self):
            global i_path
            i_path = self.ids.input_i.text
            
        def text_enter_d(self):
            global d_path
            d_path = self.ids.destination_i.text
            
            
        
        def open_folder(self):
            popup = FolderOpen(self)
            popup.open()
            
        def open_i_folder(self):
            popup = IFolderOpen(self)
            popup.open()
            
            
            
        def update_i_path(self, value):
            global i_path
            i_path = value
            
        def update_d_path(self, value):
            global d_path
            d_path = value
            
            
            
        def install(self):
            if (d_path != '' and i_path != ''):

                import_winget()

            else:
                print("felugró")
        
        