
# coding: utf-8

# In[115]:


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

from IPython.display import clear_output

import matplotlib.pyplot as plt
import numpy as np


# In[126]:

class Class_Plot_Menu (object) :
    def __init__(self,inputSig, samplingRate = 1, start = 0, end = 100):
    
        # Texte
        self.RS_Ploteinstellungen = 'Diagrammeinstellungen'
        self.RS_X_Aches_Einstellungen = 'X-Aches-Einstellungen'
        self.RS_Y_Aches_Einstellungen = 'Y-Aches-Einstellungen'
        
        
        
        self.RS_Diagrammtitel = 'Diagrammmtitel'
        self.RS_x_Achse_Titel = 'X Achsentitel'
        self.RS_y_Achse_Titel = 'Y Achsentitel'
        
        
        self.RS_Linien_Staerke = 'Linienstärke'
        self.RS_Marker_Groeße = 'Markergröße'
        self.RS_Baseline_Staerke = 'Baseline-Stärke'
        
        self.RS_Linien_Farbe = 'Linienfarbe'
        self.RS_Marker_Farbe = 'Markerfarbe'
        self.RS_Baseline_Farbe = 'Baselinefarbe'
        
        self.RS_x_Min = 'x Minimum'
        self.RS_x_Max = 'x Maximum'
        
        self.RS_y_Min = 'y Minimum'
        self.RS_y_Max = 'y Maximum'
        
        self.RS_Plot = 'Diagramm anzeigen'
        self.RS_Clear = 'Diagramme löschen'
        
        self.RS_Show_Grid = 'Grid anzeigen'
        # Variablen
        
        self.Fsignal = inputSig
        self.FsamplingRate = samplingRate

        
        # Widgets
        self.F_wdg_Layout = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')        
        
        
        
            # Allgemeines
         
        self.Ftxt_Diagrammtitle = Text(layout=self.F_wdg_Layout,visible = True) 
        self.FCol_Line = ColorPicker(concise=False,value='blue')   
        self.FFloat_Linewidth =FloatText(layout=self.F_wdg_Layout,value=1, disabled=False)
        self.FFloat_Baselinewidth =FloatText(layout=self.F_wdg_Layout,value=2, disabled=False)
        self.FFloat_Markersize =FloatText(layout=self.F_wdg_Layout,value=2, disabled=False)
        self.FCol_Marker = ColorPicker(concise=False,value='blue')     
        self.FCol_Baseline = ColorPicker(concise=False,value='blue')     
        self.Fbol_Show_Grid = Checkbox(value=False,    disabled=False)
        
        self.FBoxAllgemeinItems = []
        self.FBoxAllgemein = None      

        self.FFloat_Abtastfrequenz = FloatText(layout=self.F_wdg_Layout, value=100, disabled=False)
        
            # X Achse
        self.Ftxt_x_Achse_Titel = Text(layout=self.F_wdg_Layout,visible = True)     
        self.FFloat_x_Min =FloatText(layout=self.F_wdg_Layout,value=-1, disabled=False)    
        self.FFloat_x_Max =FloatText(layout=self.F_wdg_Layout,value=1, disabled=False)
            
        self.FBoxXAchseItems  = []  
        self.FBoxXAchse = None
            # Y Achse
            
        self.Ftxt_y_Achse_Titel = Text(layout=self.F_wdg_Layout,visible = True)    
        self.FFloat_y_Min =FloatText(layout=self.F_wdg_Layout,value=-1, disabled=False)    
        self.FFloat_y_Max =FloatText(layout=self.F_wdg_Layout,value=1, disabled=False)    
        self.FBoxYAchseItems  = []  
        self.FBoxYAchse = None    
            
            # P Plotten
        self.Fbtn_plot = Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Plot)    
        
        self.Fbtn_clear  = Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Clear)    
        self.FBoxDoPlotItems  = []  
        self.FBoxDoPlot = None  
        
        


        self.FAccItems = []
        self.FAcc = None
        
        self.show()
        
    def Copy_Input(self):
       
    
         plt.title(self.Ftxt_Diagrammtitle.value)
         plt.xlabel(self.Ftxt_x_Achse_Titel.value)
         plt.ylabel(self.Ftxt_y_Achse_Titel.value)
         plt.grid(self.Fbol_Show_Grid.value)
    
         plt.ylim([self.FFloat_y_Min.value,self.FFloat_y_Max.value])
         plt.xlim([self.FFloat_x_Min.value,self.FFloat_x_Max.value])
        
    def btn_Event_show_plot(self,ADummy):

        if self.Fsignal.FTyp ==  self.Fsignal.RS_Typ_discrete:
            # if self.Fsignal.FFunction != None:
                xValues = np.arange(self.FFloat_x_Min.value, self.FFloat_x_Max.value, 1 / self.FFloat_Abtastfrequenz.value)
                yValues = self.Fsignal.getList(xValues)

                markerline, stemlines, baseline = plt.stem( xValues,yValues, '-.')  
                
                plt.setp(markerline, linewidth=self.FFloat_Markersize.value, color=self.FCol_Marker.value)
                plt.setp(stemlines, linewidth=self.FFloat_Linewidth.value, color=self.FCol_Line.value)
                plt.setp(baseline, linewidth=self.FFloat_Baselinewidth.value,color=self.FCol_Baseline.value)
                self.Copy_Input()
    
                plt.show()
        elif self.Fsignal.FTyp == self.Fsignal.RS_Typ_continuous:
            return  None           
        elif self.Fsignal.FTyp == self.Fsignal.RS_Typ_complex:
          #  if self.Fsignal.FComplex  != None:
                 Z = self.Fsignal.getZ(True)
                 plt.arrow(0,0, Z.real, Z.imag,linewidth=self.FFloat_Linewidth.value,color=self.FCol_Line.value,
                           head_width=self.FFloat_Markersize.value/2, head_length=self.FFloat_Markersize.value,
                           )
                 self.Copy_Input()
                 plt.show()
                      
#            return  None
#        else:
#            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
        
        
         
           
            
        

    def btn_Event_clear(self,ADummy):    
        clear_output()
    
    def show(self):      
        

        
        self.Fbtn_plot.on_click(self.btn_Event_show_plot) 
        self.Fbtn_clear.on_click(self.btn_Event_clear) 
        
        
        subHBox_1_items = [Text(layout=self.F_wdg_Layout, value=self.RS_Linien_Farbe,disabled=True, visible = True),
                           Text(layout=self.F_wdg_Layout, value=self.RS_Linien_Staerke,disabled=True, visible = True)
                          ]
        subHBox_1 = HBox(children = subHBox_1_items )
        
        subHBox_2_items = [self.FCol_Line,
                           self.FFloat_Linewidth
                          ]                           
        subHBox_2 = HBox(children = subHBox_2_items )        
        
   
        
              
        
        
        
        if self.Fsignal.FTyp ==  self.Fsignal.RS_Typ_discrete:
            subHBox_3_items = [Text(layout=self.F_wdg_Layout, value=self.RS_Marker_Farbe,disabled=True, visible = True),
                               Text(layout=self.F_wdg_Layout, value=self.RS_Marker_Groeße,disabled=True, visible = True)
                              ]                           
            subHBox_3 = HBox(children = subHBox_3_items )        
        
            subHBox_4_items = [self.FCol_Marker,                         
                               self.FFloat_Markersize
                              ]                           
            subHBox_4 = HBox(children =  subHBox_4_items )        
        

            subHBox_5_items = [Text(layout=self.F_wdg_Layout, value=self.RS_Baseline_Farbe,disabled=True, visible = True),
                           Text(layout=self.F_wdg_Layout, value=self.RS_Baseline_Staerke,disabled=True, visible = True),
                          ]                           
            subHBox_5 = HBox(children =  subHBox_5_items )  
            subHBox_6_items = [self.FCol_Baseline,
                            self.FFloat_Baselinewidth
                          ]                           
            subHBox_6 = HBox(children = subHBox_6_items) 
            
            self.FBoxAllgemeinItems = [ Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel,disabled=True, visible = True),
                                        self.Ftxt_Diagrammtitle,
                                        subHBox_1,
                                        subHBox_2,
                                        subHBox_3,
                                        subHBox_4,
                                        subHBox_5,
                                        subHBox_6,
                                        Text(layout=self.F_wdg_Layout, value=self.RS_Show_Grid,disabled=True, visible = True),                                   
                                        self.Fbol_Show_Grid, Text(layout=self.F_wdg_Layout, value="Abtastfrequenz", disabled=True), self.FFloat_Abtastfrequenz                                  
                                      ]
            
        else:
            
            subHBox_3_items = [
                               Text(layout=self.F_wdg_Layout, value=self.RS_Marker_Groeße,disabled=True, visible = True)
                              ]                           
            subHBox_3 = HBox(children = subHBox_3_items )        
        
            subHBox_4_items = [                   
                               self.FFloat_Markersize
                              ]  
            subHBox_4 = HBox(children =  subHBox_4_items )              
            
            self.FBoxAllgemeinItems = [ Text(layout=self.F_wdg_Layout, value=self.RS_Diagrammtitel,disabled=True, visible = True),
                                        self.Ftxt_Diagrammtitle,
                                        subHBox_1,
                                        subHBox_2,
                                        subHBox_3,
                                        subHBox_4,

                                        Text(layout=self.F_wdg_Layout, value=self.RS_Show_Grid,disabled=True, visible = True),                                   
                                        self.Fbol_Show_Grid                                  
                                      ]            
            
            

     
        
        
 
      
        self.FBoxAllgemein = VBox(children = self.FBoxAllgemeinItems)
        
        
        self.FBoxXAchseItems =  [   Text(layout=self.F_wdg_Layout, value=self.RS_x_Achse_Titel,disabled=True, visible = True),
                                    self.Ftxt_x_Achse_Titel,                                 
                                    Text(layout=self.F_wdg_Layout, value=self.RS_x_Min,disabled=True, visible = True),
                                    self.FFloat_x_Min,
                                    Text(layout=self.F_wdg_Layout, value=self.RS_x_Max,disabled=True, visible = True),
                                    self.FFloat_x_Max
                                ]          
        
        self.FBoxXAchse = VBox(children = self.FBoxXAchseItems)
        
        self.FBoxYAchseItems =  [   Text(layout=self.F_wdg_Layout, value=self.RS_y_Achse_Titel,disabled=True, visible = True),
                                    self.Ftxt_y_Achse_Titel,
                                    Text(layout=self.F_wdg_Layout, value=self.RS_y_Min,disabled=True, visible = True),
                                    self.FFloat_y_Min,
                                    Text(layout=self.F_wdg_Layout, value=self.RS_y_Max,disabled=True, visible = True),
                                    self.FFloat_y_Max
                                ]          
        self.FBoxYAchse = VBox(children = self.FBoxYAchseItems)
        

        subHBox_7_items =[self.Fbtn_plot,self.Fbtn_clear]
        subHBox_7 = HBox(children = subHBox_7_items)       
        self.FBoxDoPlotItems  = [subHBox_7]  
        self.FBoxDoPlot = VBox(children = self.FBoxDoPlotItems)                          
        
    
    
        self.FAccItems = [self.FBoxAllgemein,self.FBoxXAchse,self.FBoxYAchse,self.FBoxDoPlot]   
    
    
        self.FAcc = Accordion(children=self.FAccItems)
        
        self.FAcc.set_title(0, self.RS_Ploteinstellungen)
        self.FAcc.set_title(1, self.RS_X_Aches_Einstellungen)
        self.FAcc.set_title(2, self.RS_Y_Aches_Einstellungen)    
        self.FAcc.set_title(3, self.RS_Plot)    
        display(self.FAcc)       
        


# In[ ]:



