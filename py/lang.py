from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import os


cwd = os.getcwd()
lang_cwd = cwd + "\lib\lang"

languages = []
with open(lang_cwd+"\lang_menu.txt","r",encoding="utf8") as file:
    for line in file:
        languages.append(list(line.split()))
file.close()
        
lang_qna = []
content= ''
with open(lang_cwd+"\lang_qna.txt","r",encoding="utf8") as file:
    for line in file:
        lang_qna.append(list(line.split(";")))



def Lang():
    class Language(Screen):
        
        def english(self):
            for  i, widget in enumerate(self.ids.items()):                  #kicseréli angolra a nyelvi beállításokat
                widget[1].text = languages[0][i]
                
            other_screen = self.manager.get_screen('qna')                   #kicseréli a qna vissza gomb nyelvét
            for i,widget in enumerate(other_screen.ids.items()):
                widget[1].text = lang_qna[0][i].replace("\\n", "\n")
    
                
        def hungarian(self):
            
            for  i, widget in enumerate(self.ids.items()):
                widget[1].text = languages[1][i]
                
            other_screen = self.manager.get_screen('qna')
            for i,widget in enumerate(other_screen.ids.items()):
                widget[1].text = lang_qna[1][i].replace("\\n", "\n")
        
        def german(self):
            
            for  i, widget in enumerate(self.ids.items()):
                widget[1].text = languages[2][i]
                
                
            other_screen = self.manager.get_screen('qna')
            for i,widget in enumerate(other_screen.ids.items()):
                widget[1].text = lang_qna[2][i].replace("\\n", "\n")
        
        def russian(self):
            
            for  i, widget in enumerate(self.ids.items()):
                widget[1].text = languages[3][i]
        
            other_screen = self.manager.get_screen('qna')
            for i,widget in enumerate(other_screen.ids.items()):
                widget[1].text = lang_qna[3][i].replace("\\n", "\n")
                    
                    
        def italian(self):
            
            for  i, widget in enumerate(self.ids.items()):
                widget[1].text = languages[4][i]
                
            other_screen = self.manager.get_screen('qna')
            for i,widget in enumerate(other_screen.ids.items()):
                widget[1].text = lang_qna[4][i].replace("\\n", "\n")
                
  
        def spanish(self):
            
            for  i, widget in enumerate(self.ids.items()):
                widget[1].text = languages[5][i]
                
            other_screen = self.manager.get_screen('qna')
            for i,widget in enumerate(other_screen.ids.items()):
                widget[1].text = lang_qna[5][i].replace("\\n", "\n")
                
            
        def japan(self):
            
            for  i, widget in enumerate(self.ids.items()):
                widget[1].text = languages[6][i]
                
            other_screen = self.manager.get_screen('qna')
            for i,widget in enumerate(other_screen.ids.items()):
                widget[1].text = lang_qna[6][i].replace("\\n", "\n")
            
                
        
        