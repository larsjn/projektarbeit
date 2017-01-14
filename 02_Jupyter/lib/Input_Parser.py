
# coding: utf-8

from IPython.display import display
from IPython.display import clear_output

from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import Text


class Class_Input_Parser(object):
    def __init__(self):
        self.RS_Titel = 'Funktionseingabe'
       
        self.F_wdg_Layout = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')
        
        self.Ftxt_Input = Text(layout=self.F_wdg_Layout,visible = True) 
        self.FInput = None
        self.FAccItems = [self.Ftxt_Input]
        self.FAcc =  Accordion(children=self.FAccItems) 
        
        self.create()
    
    def txt_Event_Eingabe (self,ADummy):
        self.FInput = self.Ftxt_Input.value       
    
    def create(self):
        self.Ftxt_Input.observe(self.txt_Event_Eingabe)
        
        self.FAcc.set_title(0, self.RS_Titel)
        display(self.FAcc)  

