# coding: utf-8

from IPython.display import display
from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import Text
from ipywidgets import Box

# Hinweise:
#   - übergabe Parameter wurden mit einem A vor dem Namen gekennzeichnet
#   - def übergreifende Variablen wurden zunächst alle in der Init vor definiert
#            o  def übergreifende Variablen wurden mit einem F vor dem Namen gekennzeichnet
#   - Texte die angezeigt werden wurden in der Init definiert und mit RS_ gekennzeichnet 
#            o  wenn Widget im Init definiert wurde ggf. der String direckt im Widget definiert


#Erzeugt die Eingabemaske für die eingabe einer kontinuierlichen (bzw. diskretisierbaren) Funktion
class Class_Input_Parser(object):
    def __init__(self,Kontinuierlich):
    # =============================================== verwendete Texte ===============================================
        if Kontinuierlich:
            self.RS_Titel = 'Eingabe eines kontinuierlichen Signals'
        else:
            self.RS_Titel = 'Eingabe eines diskreten Signals'

            
        self.RS_Eingabe     = 'y(t) ='
        self.RS_Hinweise    = 'Symbol für X-Werte: t  , Symbol für PI: pi , Eingaben werden automatisch übernommen'     
        self.RS_Default_Fkt = 'sin(2*pi*t)'

  

              
    # =============================================== def übergreifende Widgets  ===============================================       
        # Layouteinstellungen der Widgets
        self.F_wdg_Layout       = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout   = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')
        # Eingabe Widget für Nutzer
        self.Ftxt_Input         = Text(layout=self.F_wdg_Layout,visible = True, value = self.RS_Default_Fkt)         
        # Accordion mit den Widgets
        self.FAccItems          = [Box([Text(layout=self.F_wdg_Layout, value=self.RS_Eingabe,disabled=True, visible = True),self.Ftxt_Input])]                         
        self.FAcc               =  Accordion(children=self.FAccItems) 

    # =============================================== def übergreifende Variablen ===============================================      
        self.FInput = self.Ftxt_Input.value       # Speichern des Inputs für den Parser. Für den zugriff von ausßen gedacht
                                                  # Hier kann die Eingabe abgefragt werden
    # =============================================== nach init auszuführende def  ===============================================
        # Events zuweisen, und Accordion erstellen 
        self.create()
# ----------------------------------------------- ENDE DEF -----------------------------------------------     
    #Speichern des Inputs für den Parser erfolgt bei jeder änderung der Eingabe erneut
    def txt_Event_Eingabe (self,ADummy):
        self.FInput = self.Ftxt_Input.value       
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    #Anzeigen der Eingabemaske        
    def create(self):
        # Events zuweisen
        self.Ftxt_Input.observe(self.txt_Event_Eingabe)
        
        # Accordion erstellen
        self.FAcc.set_title(0, self.RS_Titel)
        print(self.RS_Hinweise)
        display(self.FAcc)  
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++