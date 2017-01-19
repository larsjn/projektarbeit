# coding: utf-8

from IPython.display import display
from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import Text
from ipywidgets import Box

#Erzeugt die Eingabemaske für die eingabe einer kontinuierlichen (bzw. diskretisierbaren) Funktion
class Class_Input_Parser(object):
    def __init__(self,Kontinuierlich):
        if Kontinuierlich:
            self.RS_Titel = 'Eingabe eines kontinuierlichen Signals'
        else:
            self.RS_Titel = 'Eingabe eines diskreten Signals'
            
        self.RS_Eingabe = 'y(t) ='
        self.RS_Hinweise = 'Symbol für X-Werte: t  , Symbol für PI: pi , Eingaben werden automatisch übernommen'            
        self.F_wdg_Layout = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')
        
        self.Ftxt_Input = Text(layout=self.F_wdg_Layout,visible = True, value = 'sin(2*pi*t)') 
        self.FInput = self.Ftxt_Input.value       #Speichern des Inputs für den Parser. 
        self.FAccItems = [Box([Text(layout=self.F_wdg_Layout, value=self.RS_Eingabe,disabled=True, visible = True),self.Ftxt_Input])]                         
        self.FAcc =  Accordion(children=self.FAccItems) 
        
        self.create()
    
#Speichern des Inputs für den Parser erfolgt bei jeder änderung der Eingabe erneut
    def txt_Event_Eingabe (self,ADummy):
        self.FInput = self.Ftxt_Input.value       

#Anzeigen der Eingabemaske        
    def create(self):
        self.Ftxt_Input.observe(self.txt_Event_Eingabe)
        
        self.FAcc.set_title(0, self.RS_Titel)
        print(self.RS_Hinweise)
        display(self.FAcc)  

