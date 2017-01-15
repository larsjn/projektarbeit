
# coding: utf-8

# In[114]:

from IPython.display import display

from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import Box
from ipywidgets import VBox
from ipywidgets import HBox
from ipywidgets import Button
from ipywidgets import Text
from ipywidgets import FloatText
from ipywidgets import Tab
from ipywidgets import ColorPicker
from ipywidgets import Checkbox
from ipywidgets import Dropdown

from IPython.display import clear_output

import matplotlib.pyplot as plt
import numpy as np
from threading import Timer


# In[129]:

class create_complex(object):
    def __init__(self):      
        
        self.RS_Im = 'Imaginäranteil'
        self.RS_Re = 'Reelleranteil'
        
        self.RS_Darstellung = 'Darstellungsform'
        self.RS_Phase = 'Phase (in Grad)'
        self.RS_Betrag = 'Betrag'  
        self.RS_Eingabe = 'Eingabe einer komplexen Zahl'
        
        self.RS_Dpb_Re_Im_Darstellung = 'Algebraische Form'
        self.RS_Dpd_Betrag_Phase_Darstellung  = 'Polarform'
        self.RS_Hinweise = 'Eingaben werden automatisch übernommen'   
        
        self.RS_Plus = '+'
        self.RS_Minus = '-'
        self.FZ = None # numpy array mit komlexen zahl
        self.FIm = None
        self.FRe = None
        self.FAngle = None
        self.FAngleRad = None
        self.FAbsolute = None       
        
        self.F_wdg_Layout = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')   
        
        
        self.FDpd_Darstellung = Dropdown(   options=[self.RS_Dpb_Re_Im_Darstellung ,self.RS_Dpd_Betrag_Phase_Darstellung],
                                            value= self.RS_Dpb_Re_Im_Darstellung , disabled=False,
                                            layout=self.F_wdg_Layout
                                        )

        self.FFloat_Im = FloatText(layout=self.F_wdg_Layout,value=0.4, disabled=False)
        self.FFloat_Re = FloatText(layout=self.F_wdg_Layout,value=0, disabled=False)
        self.FFloat_Phase = FloatText(layout=self.F_wdg_Layout,value=0, disabled=False)
        self.FFloat_Betrag = FloatText(layout=self.F_wdg_Layout,value=0, disabled=False) 
        
        
        self.FHBoxAlgSubVBoxItems_1 = [  Text(layout=self.F_wdg_Layout, value=self.RS_Re,disabled=True, visible = True),
                                         self.FFloat_Re
                                      ]
        self.FHBoxAlgSubVBox_1 = VBox(layout=self.F_wdg_Layout,children=self.FHBoxAlgSubVBoxItems_1)
        
        self.FHBoxAlgSubVBoxItems_2 = [  Text(layout=self.F_wdg_Layout, value=self.RS_Im,disabled=True, visible = True),
                                         self.FFloat_Im
                                      ]
        self.FHBoxAlgSubVBox_2 = VBox(layout=self.F_wdg_Layout,children=self.FHBoxAlgSubVBoxItems_2)
        
        
        self.FHBoxPolarSubVBoxItems_1 = [  Text(layout=self.F_wdg_Layout, value= self.RS_Betrag ,disabled=True, visible = True),
                                           self.FFloat_Betrag
                                        ] 
        self.FHBoxPolarSubVBox_1 = VBox(layout=self.F_wdg_Layout,children=self.FHBoxPolarSubVBoxItems_1)
        
        self.FHBoxPolarSubVBoxItems_2 = [  Text(layout=self.F_wdg_Layout, value=self.RS_Phase,disabled=True, visible = True),
                                           self.FFloat_Phase
                                        ]
        self.FHBoxPolarSubVBox_2 = VBox(layout=self.F_wdg_Layout,children=self.FHBoxPolarSubVBoxItems_2)        
    
        self.FHBoxAlgItems    = [ self.FHBoxAlgSubVBox_1, self.FHBoxAlgSubVBox_2]
        
        self.FHBoxAlg = HBox(children=self.FHBoxAlgItems )
        
        self.FHBoxPolarItems  = [self.FHBoxPolarSubVBox_1,self.FHBoxPolarSubVBox_2]
        
        self.FHBoxPolar = HBox(children=self.FHBoxPolarItems )
                                   
        self.FEingabeSeiteItems = [ Text(layout=self.F_wdg_Layout, value= self.RS_Dpb_Re_Im_Darstellung ,disabled=True, visible = True),
                                    self.FHBoxAlg,
                                    Text(layout=self.F_wdg_Layout, value= self.RS_Dpd_Betrag_Phase_Darstellung  ,disabled=True, visible = True),
                                    self.FHBoxPolar                       
                                   ]
        
        self.FPhaseWarten = False
        self.FAlgWarten= False
        
        self.FEingabeSeite = VBox(layout=self.F_wdg_Layout,children=self.FEingabeSeiteItems)
        
        self.FAccItems  = [self.FEingabeSeite]  
        self.FAcc = Accordion(children=self.FAccItems)      
        
        self.create()
        self.Float_Event_Alg_Changed(None)  
        
    def Timer_Event(self):# Warten da sonst Schleife der Änderungen 
        self.FPhaseWarten = False
        self.FAlgWarten= False
        
    def Float_Event_Alg_Changed(self,ADummy):      


        if not self.FAlgWarten:# Warten da sonst Schleife der Änderungen
          
            self.FPhaseWarten = True             
            self.FIm = self.FFloat_Im.value
            self.FRe = self.FFloat_Re.value
            self.FZ=self.FRe+1j*self.FIm 
            self.FFloat_Phase.value = np.angle(self.FZ,True)
            self.FFloat_Betrag.value =np.absolute(self.FZ)

            self.FIm = self.FFloat_Im.value
            self.FRe = self.FFloat_Re.value
            self.FAngle = self.FFloat_Phase.value 
            self.FAngleRad = np.angle(self.FZ,False)        
            self.FAbsolute = self.FFloat_Betrag.value
            
            Timer(0.1, self.Timer_Event, ()).start()

        
    def Float_Event_Polar_Changed (self,ADummy):

        if not self.FPhaseWarten:# Warten da sonst Schleife der Änderungen
            
            self.FAlgWarten = True
            self.FFloat_Re.value = self.FFloat_Betrag.value * np.cos(np.radians(self.FFloat_Phase.value ))          
            self.FFloat_Im.value = self.FFloat_Betrag.value * np.sin(np.radians(self.FFloat_Phase.value ))             
            self.FZ=self.FFloat_Re.value+1j*self.FFloat_Im.value
            self.FIm = self.FFloat_Im.value
            self.FRe = self.FFloat_Re.value
            self.FAngle = self.FFloat_Phase.value 
            self.FAngleRad = np.angle(self.FZ,False)        
            self.FAbsolute = self.FFloat_Betrag.value
            
            Timer(0.1, self.Timer_Event, ()).start()

        
    def create(self):
       
        self.FFloat_Phase.observe(self.Float_Event_Polar_Changed)
        self.FFloat_Betrag.observe(self.Float_Event_Polar_Changed)
        self.FFloat_Im.observe(self.Float_Event_Alg_Changed)
        self.FFloat_Re.observe(self.Float_Event_Alg_Changed)                               
        self.FAcc.set_title(0, self.RS_Eingabe)
        print(self.RS_Hinweise)
        display(self.FAcc) 
    
        
        
        
        
        


# In[130]:

# create_complex()


# In[ ]:



