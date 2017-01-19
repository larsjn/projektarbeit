# coding: utf-8

import numpy as np
from IPython.display import display
from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import VBox
from ipywidgets import HBox
from ipywidgets import Text
from ipywidgets import FloatText
from ipywidgets import Dropdown
from threading import Timer

# Hinweise:
#   - übergabe Parameter wurden mit einem A vor dem Namen gekennzeichnet
#   - def übergreifende Variablen wurden zunächst alle in der Init vor definiert
#            o  def übergreifende Variablen wurden mit einem F vor dem Namen gekennzeichnet
#   - Texte die angezeigt werden wurden in der Init definiert und mit RS_ gekennzeichnet 
#            o  wenn Widget im Init definiert wurde ggf. der String direckt im Widget definiert

class create_complex(object):
    def __init__(self):      
    # =============================================== verwendete Texte ===============================================       
        self.RS_Im                            = 'Imaginäranteil'
        self.RS_Re                            = 'Reelleranteil'        
        self.RS_Darstellung                   = 'Darstellungsform'
        self.RS_Phase                         = 'Phase (in Grad)'
        self.RS_Betrag                        = 'Betrag'  
        self.RS_Eingabe                       = 'Eingabe einer komplexen Zahl'        
        self.RS_Dpb_Re_Im_Darstellung         = 'Algebraische Form'
        self.RS_Dpd_Betrag_Phase_Darstellung  = 'Polarform'
        self.RS_Hinweise                      = 'Eingaben werden automatisch übernommen'           
        self.RS_Plus                          = '+'
        self.RS_Minus                         = '-'

    # =============================================== def übergreifende Variablen ===============================================  
        self.FZ             = None # numpy array mit komlexen zahl
        self.FIm            = None
        self.FRe            = None
        self.FAngle         = None
        self.FAngleRad      = None
        self.FAbsolute      = None   
        self.FPhaseWarten   = False
        self.FAlgWarten     = False    
    # =============================================== def übergreifende Widgets  ===============================================       
        # Layouteinstellungen der Widgets
        self.F_wdg_Layout     = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')   
        
        # Widgets zur Eingabe der komplexen Zahl
        self.FFloat_Im      = FloatText(layout=self.F_wdg_Layout,value=0.4, disabled=False)
        self.FFloat_Re      = FloatText(layout=self.F_wdg_Layout,value=0, disabled=False)
        self.FFloat_Phase   = FloatText(layout=self.F_wdg_Layout,value=0, disabled=False)
        self.FFloat_Betrag  = FloatText(layout=self.F_wdg_Layout,value=0, disabled=False) 
        
        # verschiedene Boxen um die Wigets anzuordnen
        self.FHBoxAlgSubVBoxItems_1 = [  Text(layout=self.F_wdg_Layout, value=self.RS_Re,disabled=True, visible = True),
                                         self.FFloat_Re
                                      ]
        self.FHBoxAlgSubVBox_1 = VBox(layout=self.F_wdg_Layout,children=self.FHBoxAlgSubVBoxItems_1)
        
        self.FHBoxAlgSubVBoxItems_2 = [  Text(layout=self.F_wdg_Layout, value=self.RS_Im,disabled=True, visible = True),
                                         self.FFloat_Im
                                      ]
        self.FHBoxAlgSubVBox_2  = VBox(layout=self.F_wdg_Layout,children=self.FHBoxAlgSubVBoxItems_2)
        
        
        self.FHBoxPolarSubVBoxItems_1 = [  Text(layout=self.F_wdg_Layout, value= self.RS_Betrag ,disabled=True, visible = True),
                                           self.FFloat_Betrag
                                        ] 
        self.FHBoxPolarSubVBox_1 = VBox(layout=self.F_wdg_Layout,children=self.FHBoxPolarSubVBoxItems_1)
        
        self.FHBoxPolarSubVBoxItems_2 = [  Text(layout=self.F_wdg_Layout, value=self.RS_Phase,disabled=True, visible = True),
                                           self.FFloat_Phase
                                        ]
        self.FHBoxPolarSubVBox_2 = VBox(layout=self.F_wdg_Layout,children=self.FHBoxPolarSubVBoxItems_2)        
    
        self.FHBoxAlgItems = [ self.FHBoxAlgSubVBox_1, self.FHBoxAlgSubVBox_2]
        
        self.FHBoxAlg = HBox(children=self.FHBoxAlgItems )
        
        self.FHBoxPolarItems = [self.FHBoxPolarSubVBox_1,self.FHBoxPolarSubVBox_2]
        
        self.FHBoxPolar = HBox(children=self.FHBoxPolarItems )
                                   
        self.FEingabeSeiteItems = [ Text(layout=self.F_wdg_Layout, value= self.RS_Dpb_Re_Im_Darstellung ,disabled=True, visible = True),
                                    self.FHBoxAlg,
                                    Text(layout=self.F_wdg_Layout, value= self.RS_Dpd_Betrag_Phase_Darstellung  ,disabled=True, visible = True),
                                    self.FHBoxPolar                       
                                   ]      
      
        self.FEingabeSeite = VBox(layout=self.F_wdg_Layout,children=self.FEingabeSeiteItems)
        

        # Accordion mit den Widgets
        self.FAccItems  = [self.FEingabeSeite]  
        self.FAcc = Accordion(children=self.FAccItems)    
  
    # =============================================== nach init auszuführende def  ===============================================
        # Anzeigen des Widgets, Events zuweisen
        self.create()
        # Übernahme der Init-komplexen-Zahl
        self.Float_Event_Alg_Changed(None)  
# ----------------------------------------------- ENDE DEF -----------------------------------------------        
    # Warten da sonst Schleife der Änderungen 
    def Timer_Event(self):
        self.FPhaseWarten = False
        self.FAlgWarten= False
# ----------------------------------------------- ENDE DEF -----------------------------------------------        
    # Umrechnen und Speichern der Zahl  Alg --> Polar
    def Float_Event_Alg_Changed(self,ADummy):      


        if not self.FAlgWarten:# Warten da sonst Schleife der Änderungen          
            self.FPhaseWarten = True 
            
            self.FIm                 = self.FFloat_Im.value
            self.FRe                 = self.FFloat_Re.value
            self.FZ                  =self.FRe+1j*self.FIm 
            self.FFloat_Phase.value  = np.angle(self.FZ,True)
            self.FFloat_Betrag.value =np.absolute(self.FZ)
            # Umrechnen in andre Darstellungsform
            self.FIm        = self.FFloat_Im.value
            self.FRe        = self.FFloat_Re.value
            self.FAngle     = self.FFloat_Phase.value 
            self.FAngleRad  = np.angle(self.FZ,False)        
            self.FAbsolute  = self.FFloat_Betrag.value
            
            # Timer um zuverhindern das eine Schleife der Umrechnungen entsteht
            Timer(0.1, self.Timer_Event, ()).start()
# ----------------------------------------------- ENDE DEF -----------------------------------------------         
    # Umrechnen und Speichern der Zahl  Polar --> Alg
    def Float_Event_Polar_Changed (self,ADummy):

        if not self.FPhaseWarten:# Warten da sonst Schleife der Änderungen            
            self.FAlgWarten = True

            # Umrechnen in andre Darstellungsform
            self.FFloat_Re.value = self.FFloat_Betrag.value * np.cos(np.radians(self.FFloat_Phase.value ))          
            self.FFloat_Im.value = self.FFloat_Betrag.value * np.sin(np.radians(self.FFloat_Phase.value ))             
            self.FZ              = self.FFloat_Re.value+1j*self.FFloat_Im.value
            
            self.FIm        = self.FFloat_Im.value
            self.FRe        = self.FFloat_Re.value
            self.FAngle     = self.FFloat_Phase.value 
            self.FAngleRad  = np.angle(self.FZ,False)        
            self.FAbsolute  = self.FFloat_Betrag.value
            
            # Timer um zuverhindern das eine Schleife der Umrechnungen entsteht
            Timer(0.1, self.Timer_Event, ()).start()
# ----------------------------------------------- ENDE DEF -----------------------------------------------         
    # Widget erzeugen und Events zuweisen
    def create(self):
        # Events zuweisen
        self.FFloat_Phase.observe(self.Float_Event_Polar_Changed)
        self.FFloat_Betrag.observe(self.Float_Event_Polar_Changed)
        self.FFloat_Im.observe(self.Float_Event_Alg_Changed)
        self.FFloat_Re.observe(self.Float_Event_Alg_Changed)   

        # Arrcordion erzeugen                    
        self.FAcc.set_title(0, self.RS_Eingabe)
        print(self.RS_Hinweise)
        display(self.FAcc)     
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++       
        
        
        
        



