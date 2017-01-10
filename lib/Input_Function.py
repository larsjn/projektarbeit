
# coding: utf-8

# In[ ]:




# In[3]:

from __future__ import print_function


from IPython.display import display

from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import Box
from ipywidgets import VBox
from ipywidgets import HBox
from ipywidgets import Button
from ipywidgets import Text
from ipywidgets import IntSlider
from ipywidgets import Dropdown
from ipywidgets import IntText
from ipywidgets import FloatText
from ipywidgets import Tab
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pyplot import figure, show
import matplotlib._pylab_helpers
import sys



# In[4]:

class Class_btn_Menu (object) :
    
    def __init__(self,AxValues, ACurrentValue,Atxt_All_Input,AIsSub,AForwardOperator,AForwardFkt, ADefNewTab, ADefDeleteTab, ASubCount): 
        self.FEnableDebugPrint = False
        
        if self.FEnableDebugPrint:
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: AxValues         ' + str(AxValues ))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: ACurrentValue    ' + str(ACurrentValue))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: Atxt_All_Input   ' + str(Atxt_All_Input ))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: AIsSub           ' + str(AIsSub ))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: AForwardOperator ' + str(AForwardOperator ))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: AForwardFkt      ' + str(AForwardFkt ))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: ADefNewTab       ' + str(ADefNewTab ))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: ADefDeleteTab    ' + str(ADefDeleteTab ))
                print('Fenster Nr: ' + str(ASubCount) +':' +'Debug: Init: ASubCount        ' + str(ASubCount ))
                
        # ====================================== Definition der Angezeigten Texte ====================================== 
#         Tracer()() #this one triggers the debugger ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        self.RS_Help_Class = 'Gibt Erzeugt mittels "btn_BTNMenu_erstellen" das Button Menu zur eingabe von Funktionen zurück'
        # Texte 
        self.RS_Funktion='Funktion:'
        self.RS_Anzahl='Anzahl:'
        self.RS_Nichts = ''
        self.RS_Titel_Setup_Funktion = 'Anzahl der Teil Funktionen und Operatoren'
        self.RS_Titel_Typ_Funktion = 'Typ der Funktion'
        self.RS_Titel_Mask_Funktion = 'Eingabe der Funktion: Hinweis Variable mit "x" eintragen'
        self.RS_Zahl = 'Zahl' 
        self.RS_Symbol_fue_X_Werte = 't'
        self.RS_Plus = '+'
        self.RS_Minus = '-'
        self.RS_Mul = '*'
        self.RS_Div = '/'
        self.RS_Sin = 'Sin('
        self.RS_Cos = 'Cos('
        self.RS_Klammer_auf = '('
        self.RS_Klammer_zu =')'    
        # ====================================== Definition "def" übergreifende Variablen ======================================
        self.FxWerte = AxValues
        self.FNutzeXWerte = False
        self.FBefehl = None
        self.FInputA = None
        self.FInputB = None
        self.FIsSub  = AIsSub
        self.FSubFirstNum = True
        self.FCurrentValue = ACurrentValue
        self.FSubCurrentValue = None 
        self.FDefNewTab=ADefNewTab
        self.FDefDeleteTab=ADefDeleteTab
        self.FForwardOperator=AForwardOperator
        self.FForwardFkt=AForwardFkt
        self.FOperator= None
        self.FFkt= None
        self.FSubCount = str(ASubCount)
        # ====================================== Definition "def" übergreifende Widgets ====================================== 
        self.F_wdg_Layout = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')
        
        self.Fbtn_Add = Button(layout=self.F_wdg_Layout,button_style='warning',description='Add')
        
        self.Fbtn_Sub = Button(layout=self.F_wdg_Layout,button_style='warning',description='Sub')
        
        self.Fbtn_Mul = Button(layout=self.F_wdg_Layout,button_style='warning',description='Mul')
        
        self.Fbtn_Div = Button(layout=self.F_wdg_Layout,button_style='warning',description='Div')        

        self.Fbtn_Num = Button(layout=self.F_wdg_Layout,button_style='warning',description='Zahl')
        
        self.Fbtn_Cos = Button(layout=self.F_wdg_Layout,button_style='warning',description='Cos')
        
        self.Fbtn_Sin = Button(layout=self.F_wdg_Layout,button_style='warning',description='Sin')
        
        self.Fbtn_Klammer = Button(layout=self.F_wdg_Layout,button_style='warning',description='Klammer')

        self.Fbtn_Eingeben = Button(layout=self.F_wdg_Layout,button_style='warning',description='Weiter')   
        if self.FIsSub:
            self.Fbtn_KlammerZu = Button(layout=self.F_wdg_Layout,button_style='warning',description='Klammer schließen')
        else:
            self.Fbtn_KlammerZu = Button(layout=self.F_wdg_Layout,button_style='warning',description='Fertig')
        self.Fbtn_x_Werte_Einfuegen = Button(layout=self.F_wdg_Layout,button_style='warning',description='x-Werte einfügen')   
        self.Ftxt_Num = FloatText(Layout=self.F_wdg_Layout,value=1, description=self.RS_Zahl, disabled=False)
        self.Ftxt_All_Input = Atxt_All_Input
# ---------------------------------------------------- End def -----------------------------------------------------     
    def __exit__(self, exc_type, exc_value, traceback):
        self.package_obj.cleanup()             
# ---------------------------------------------------- End def -----------------------------------------------------
    def help(self,ADummy):       
        print(self.RS_Help_Class) 
# ---------------------------------------------------- End def -----------------------------------------------------
    def Switch_Case_für_Numpy(self,ADummy): 
        if  self.FBefehl == None:
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Switch_Case_für_Numpy: Befehl: None'  )
        else:
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Switch_Case_für_Numpy: Befehl: ' + self.FBefehl )
            
        if self.FBefehl == self.RS_Plus :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Plus')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) ) 
            if self.FIsSub:
                self.FSubCurrentValue = np.add(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue))
            else:
                self.FCurrentValue = np.add(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentValue))
      
           
            
        if self.FBefehl == self.RS_Minus :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Minus')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) ) 
            if self.FIsSub:
                self.FSubCurrentValue = np.subtract(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue))
            else:
                self.FCurrentValue = np.subtract(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentValue)) 
         
            
            
        if self.FBefehl == self.RS_Mul :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Mul')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) ) 
            if self.FIsSub:
                self.FSubCurrentValue = np.multiply(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue)) 
            else:
                self.FCurrentValue = np.multiply(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentValue)) 
                
           
            
            
        if self.FBefehl == self.RS_Div :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Div')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) ) 
            if self.FIsSub:
                self.FSubCurrentValue = np.divide(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue)) 
            else:
                self.FCurrentValue = np.divide(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentValue)) 
            
            
            
        if self.FBefehl == self.RS_Cos :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Cos')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) ) 
            if self.FIsSub:
                self.FSubCurrentValue = np.cos(self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue)) 
            else:
                self.FCurrentValue = np.cos(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentValue)) 
           
     
            
        if self.FBefehl == self.RS_Sin :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Sin')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) ) 
            if self.FIsSub:
                self.FSubCurrentValue = np.sin(self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue)) 
            else:
                self.FCurrentValue = np.sin(self.FInputA,self.FInputB)
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentValue)) 
            
            
            
        if self.FBefehl == self.RS_Klammer_auf :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Klammer')
           
            
            
        if self.FBefehl == None : 
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Switch-Default')
            if self.FIsSub:
                self.FSubCurrentValue = self.FInputB
# ---------------------------------------------------- End def -----------------------------------------------------
    def KlammerSchließen(self,ADummy):
         if self.FIsSub:            
                           
            self.FInputA = self.FCurrentValue
            self.FInputB = self.FSubCurrentValue 
            self.FBefehl = self.FForwardFkt
            self.Switch_Case_für_Numpy(None)
            
            self.FInputA = self.FCurrentValue
            self.FInputB = self.FSubCurrentValue            
            self.FBefehl = self.FForwardOperator
            self.Switch_Case_für_Numpy(None)    
            self.FCurrentValue = self.FSubCurrentValue 
            
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue) +'als CurrentValue gesetzt ') 
        
        
# ---------------------------------------------------- End def -----------------------------------------------------
    def Enable_btn (self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Enable_btn ')
        self.Fbtn_Num.disabled = False
        self.Fbtn_Cos.disabled = False        
        self.Fbtn_Sin.disabled  = False
        self.Fbtn_Klammer.disabled  = False
#         self.Fbtn_Eingeben.disabled  = False  
# ---------------------------------------------------- End def -----------------------------------------------------        
    def Enable_left_btn (self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Enable_btn ')
        self.Fbtn_Add.disabled = False
        self.Fbtn_Sub.disabled = False
        self.Fbtn_Mul.disabled = False
        self.Fbtn_Div.disabled = False
# ---------------------------------------------------- End def -----------------------------------------------------
    def disable_btn (self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: disable_btn ')
        self.Fbtn_Add.disabled = True
        self.Fbtn_Sub.disabled = True
        self.Fbtn_Mul.disabled = True
        self.Fbtn_Div.disabled = True
        self.Fbtn_Num.disabled = True
        self.Fbtn_Cos.disabled = True        
        self.Fbtn_Sin.disabled  = True
        self.Fbtn_Klammer.disabled  = True
        self.Fbtn_Eingeben.disabled  = True 
        self.Fbtn_x_Werte_Einfuegen.disabled = True 
        self.Fbtn_KlammerZu.disabled  = True 
        self.Ftxt_Num.disabled  = True          
        
# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_Plus(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Plus) 
        self.disable_btn(None)
        self.Enable_btn(None)    
        self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Plus
        self.FBefehl = self.RS_Plus
        self.FOperator= self.FBefehl
# ---------------------------------------------------- End def -----------------------------------------------------               
    def btn_Event_Minus(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Minus) 
        self.disable_btn(None)
        self.Enable_btn(None)    
        self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Minus
        self.FBefehl = self.RS_Minus
        self.FOperator= self.FBefehl
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Mul(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Mul) 
        self.disable_btn(None)
        self.Enable_btn(None)    
        self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Mul
        self.FBefehl = self.RS_Mul
        self.FOperator= self.FBefehl
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Div(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Div)         
        self.disable_btn(None)
        self.Enable_btn(None)    
        self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Div
        self.FBefehl = self.RS_Div
        self.FOperator= self.FBefehl
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Num(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Zahl')   
        self.disable_btn(None)
        self.Fbtn_Eingeben.disabled  = False 
        self.Ftxt_Num.disabled  = False 
        if self.FIsSub :
            if self.FSubFirstNum :
                self.FSubFirstNum = False
                self.FSubCurrentValue = self.Ftxt_Num.value 
                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue)) 

        self.Fbtn_Eingeben.disabled  = False
        self.Fbtn_x_Werte_Einfuegen.disabled  = False
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Sin(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Sin) 
            
        self.FFkt=self.RS_Sin
        if self.FIsSub :            
            self.FDefNewTab(self.FOperator,self.FFkt,self.FSubCurrentValue)
        else:
            self.FDefNewTab(self.FOperator,self.FFkt,self.FCurrentValue)
        
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Cos(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Cos)
        alterBefehl = self.FBefehl 
        self.FBefehl = self.RS_Cos
        self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Cos
        self.disable_btn(None)
        self.FFkt=self.RS_Cos
        if self.FIsSub :            
            self.FDefNewTab(self.FOperator,self.FFkt,self.FSubCurrentValue)
        else:
            self.FDefNewTab(self.FOperator,self.FFkt,self.FCurrentValue)
        
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Klammer_auf(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Klammer_auf) 
        self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Klammer_auf
        alterBefehl = self.FBefehl 
        self.FBefehl = self.RS_Klammer_auf
        self.disable_btn(None)        
        self.FFkt=self.RS_Klammer_auf
        if self.FIsSub :            
            self.FDefNewTab(self.FOperator,self.FFkt,self.FSubCurrentValue)
        else:
            self.FDefNewTab(self.FOperator,self.FFkt,self.FCurrentValue)
        
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Weiter(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount+ ':' +'Debug: btn_Event_Weiter')
        self.Fbtn_KlammerZu.disabled  = False   
        if self.FIsSub :
            self.Enable_left_btn(None) 
            self.FInputA = self.FSubCurrentValue
            if self.FNutzeXWerte:
                self.FInputB = self.FxWerte
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Symbol_fue_X_Werte 
                self.FNutzeXWerte = False
            else:
                self.FInputB = self.Ftxt_Num.value 
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + str(self.FInputB) 
                    
            self.Switch_Case_für_Numpy(None) 

        else:            
            self.FInputA = self.FCurrentValue
            if self.FNutzeXWerte:
                self.FInputB = self.FxWerte
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Symbol_fue_X_Werte 
                self.FNutzeXWerte = False
            else:
                self.FInputB = self.Ftxt_Num.value 
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + str(self.FInputB) 
            self.Switch_Case_für_Numpy(None)        


            self.Enable_left_btn(None)
            self.Fbtn_Eingeben.disabled  = True
            self.Fbtn_x_Werte_Einfuegen.disabled   = True
#             self.FDefDeleteTab(None) 
# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_x_Werte_einfuegen(self,ADummy):
        self.FNutzeXWerte = True
        self.btn_Event_Weiter(None)
        self.Fbtn_Eingeben.disabled  = True
        self.Fbtn_x_Werte_Einfuegen.disabled   = True
# ---------------------------------------------------- End def -----------------------------------------------------  
    def btn_Event_Klammer_zu(self,ADummy):
        self.FInputB = self.Ftxt_Num.value
        if self.FIsSub :  
            self.FInputA = self.FSubCurrentValue
            self.KlammerSchließen(None);
            self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + ')'
        else:
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount+ ':' +'Debug: ###################################################')
#             self.FInputA = self.FCurrentValue 
#             self.Switch_Case_für_Numpy(None)
      
        
       
        self.Enable_left_btn(None)
        self.Fbtn_Eingeben.disabled  = True
        self.FDefDeleteTab(None)
       
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Klammer_zu) 
# ---------------------------------------------------- End def -----------------------------------------------------  
        
    def btn_BTNMenu_erstellen (self,ADisable_btn_left):        
#         Tracer()() #this one triggers the debugger ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
        
        self.Fbtn_Add.on_click( self.btn_Event_Plus )
        self.Fbtn_Sub.on_click( self.btn_Event_Minus )
        self.Fbtn_Div.on_click( self.btn_Event_Div )
        self.Fbtn_Mul.on_click( self.btn_Event_Mul )
       
        self.Fbtn_Cos.on_click( self.btn_Event_Cos )
        self.Fbtn_Num.on_click( self.btn_Event_Num )
        self.Fbtn_Klammer.on_click( self.btn_Event_Klammer_auf )
            
        self.Fbtn_Eingeben.on_click( self.btn_Event_Weiter )              
        self.Fbtn_KlammerZu.on_click( self.btn_Event_Klammer_zu )     
        self.Fbtn_x_Werte_Einfuegen.on_click(self.btn_Event_x_Werte_einfuegen)
        
        
        self.disable_btn(None)
        self.Enable_left_btn(None)


        if ADisable_btn_left == True :
            self.disable_btn(None)
            self.Enable_btn(None)
            self.Fbtn_Eingeben.disabled  = True
            
            
        btn_links = [ self.Fbtn_Add, self.Fbtn_Sub, self.Fbtn_Mul, self.Fbtn_Div]
        btn_rechts = [ self.Fbtn_Num, self.Fbtn_Cos, self.Fbtn_Sin, self.Fbtn_Klammer]
        btn_SubHBox1 = HBox(children=[ self.Ftxt_Num,  self.Fbtn_x_Werte_Einfuegen])

        btn_SubHBox2 = HBox(children=[ self.Fbtn_Eingeben, self.Fbtn_KlammerZu])

        
        itm_rechts = [ btn_SubHBox1, btn_SubHBox2]
        btn_VBoxr = VBox(children=btn_rechts)
        btn_VBoxl = VBox(children=btn_links)
        itm_VBoxr = VBox(children=itm_rechts)

        HBoxItems = [ btn_VBoxl,btn_VBoxr,itm_VBoxr ]        
        btn_HBox = HBox(children=HBoxItems)

        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +"Debug: btn_Tab")   
        return btn_HBox


# In[41]:


class Class_Create_New_Function(object) :
    
    def __init__(self): 
        self.FEnableDebugPrint = False
        # ====================================== Definition der Angezeigten Texte ====================================== 
        # Acc Titel
        self.RS_Acc_Titel_Setup = 'Grundeinstellungen der Funktion'
        self.RS_Acc_Titel_Mask = 'Eingabe der Funktion'
        # Tab Titel
        self.RS_Tab_Titel_Main = 'Eingabe'
        self.RS_Tab_Titel_Sub  = 'Sub Eingabe : '
        # Texte 
        self.RS_Funktion='Funktion:'
        self.RS_Anzahl='Anzahl:'
        self.RS_Nichts = ''
        self.RS_Titel_Setup_Funktion = 'Anzahl der Teil Funktionen und Operatoren'
        self.RS_Titel_Typ_Funktion = 'Typ der Funktion'
        self.RS_Titel_Mask_Funktion = 'Eingabe der Funktion: Hinweis Variable mit "x" eintragen'
        self.RS_x_Werte_einfuegen = 'x-Werte einfügen'
        self.RS_Zahl = 'Zahl' 
        self.RS_Abtastfrequenz = 'Abtastfrequenz in Hz'
        self.RS_x_Array = 'Array der X-Wert'
        # Help Texte
        self.RS_Help_Class = 'Gibt Erzeugt mittels "Create_fkt_layout" die Eingabemaske zum erzeugen einer neuen Funktion'
        self.RS_Help_Setup_Funktion = '1: Widgets der Eingabemaske der ANZ, 2: Eingabemaske ANZ, 3: Widgets Eingabemaste Setup, 4: Eingabemaste Setup'

        # Button Texte
        self.RS_Btn_Eingabemaske_erzeugen = 'Eingabemaske erzeugen'
        self.RS_Btn_Weiter = 'Eingabe nutzen'
        self.RS_Btn_loeschen = 'Fenster löschen'
        self.RS_Btn_save = 'Speichern'
        self.RS_Btn_Use_x_Values = 'X-Werte nutzen'
        # Dropdown Menu Einträge
        self.RS_Dpd_Reelle_Funktion = 'Reelle Funktion'
        self.RS_Symbol_fue_X_Werte = 't'
        self.RS_Dpd_Plus = '+'
        self.RS_Dpd_Minus = '-'
        self.RS_Dpd_Mul = '*'
        self.RS_Dpd_Div = '/'
        self.RS_Dpd_Sin = 'Sin('
        self.RS_Dpd_Cos = 'Cos('
        self.RS_Dpd_Klammer_auf = '('
        self.RS_Dpd_Klammer_zu =')'       
        # ====================================== Definition "def" übergreifende Variablen ====================================== 
        self.FMaskResultIteams = None
        self.FMaskResultForm = None
        self.FCurrentValue = None
        self.FSubCurrentValue = None
        self.FxWerteAlsInit = False
        self.FListClass_btn_Menu = []
        self.FxWerte = []
        self.FyWerte = []
        # ====================================== Definition "def" übergreifende Widgets ====================================== 
        self.F_wdg_Layout = Layout(display='flex',flex_flow='row',justify_content='center')
        self.F_wdg_Box_Layout = Layout(display='flex',flex_flow='column',align_items='stretch',width='100%')
        
        self.FAccItems = []
        self.FAcc = None
        self.FFloat_Abtastfrequenz =FloatText(layout=self.F_wdg_Layout,value=10, disabled=False)
        self.Ftxt_All_Input = Text(layout=self.F_wdg_Layout, value='Eingegebene Formel', disabled=True)
        self.Ftxt_Current_Input = Text(layout=self.F_wdg_Layout, value='Aktuelle Eingabe', disabled=False)
        self.FFloat_Init_Fkt = FloatText(Layout=self.F_wdg_Layout,value=1, description=self.RS_Zahl, disabled=False)
        
        self.FTabItems = []
        self.FTab = None
        # ====================================== Widget Modul Namen ======================================
        
        
        self.Modul_Name_FloatTextModel = 'FloatTextModel'
        self.Modul_Name_DropdownModel ='DropdownModel'
        
        
        # ====================================== Definition erstellen ====================================== 
# ---------------------------------------------------- End def -----------------------------------------------------
    def help(self):       
        print(self.RS_Help_Class)    
# ---------------------------------------------------- End def -----------------------------------------------------
    def Delete_Tab(self,ADummy):
        if self.FEnableDebugPrint:
            print('Debug: Löschen Tab')  
        if len(self.FListClass_btn_Menu) > 1 :
            i = len(self.FListClass_btn_Menu) - 1
#             print(self.FListClass_btn_Menu)
#             print(self.FListClass_btn_Menu[i])
#             display(self.FListClass_btn_Menu[i])
#             self.FListClass_btn_Menu[i].close   
            self.FCurrentValue = self.FListClass_btn_Menu[i].FCurrentValue 
            if len(self.FListClass_btn_Menu) > 2 :
                self.FListClass_btn_Menu[i-1].FSubCurrentValue  = self.FListClass_btn_Menu[i].FSubCurrentValue 
            if self.FEnableDebugPrint:
                print('Debug: Delete Tab: CurrentValue:' + str(self.FCurrentValue) )
            self.FListClass_btn_Menu.pop(i)
            self.FListClass_btn_Menu[i-1].Enable_left_btn(None)
            self.FListClass_btn_Menu[i-1].Fbtn_KlammerZu.disabled = False
            self.FTabItems[i].close
            self.FTabItems.pop(i)            
            self.FTab.children = self.FTabItems             
            self.FTab.selected_index =len(self.FTabItems) - 1
        else:
            self.Create_Plot(None)
# ---------------------------------------------------- End def -----------------------------------------------------       
        
    def New_Tab(self,AForwardOperator,AForwardFkt,ACurrentValue):
        if self.FEnableDebugPrint:
            print('Debug: Neues Tab')
        i = len(self.FListClass_btn_Menu) 
        self.FListClass_btn_Menu = self.FListClass_btn_Menu + [ Class_btn_Menu(
                self.FxWerte,
                ACurrentValue,
                self.Ftxt_All_Input,
                True,
                AForwardOperator,
                AForwardFkt,
                self.New_Tab,
                self.Delete_Tab,i) ]
       
        self.FTabItems = self.FTabItems + [self.FListClass_btn_Menu[i].btn_BTNMenu_erstellen(True)]
        self.FTab.children = self.FTabItems 
        self.FTab.set_title(len(self.FTabItems) - 1, self.RS_Tab_Titel_Sub + str(i)) 
        self.FTab.selected_index =len(self.FTabItems) - 1
# ---------------------------------------------------- End def -----------------------------------------------------
    def Create_Plot(self,ADummy): 
        if self.FEnableDebugPrint:
            print('Debug: Create_Plot')
        
        if self.FListClass_btn_Menu[0].FFkt == None:
            self.FCurrentValue = self.FListClass_btn_Menu[0].FCurrentValue       

        self.FAcc.visible = False
        self.FyWerte = self.FCurrentValue      

# ---------------------------------------------------- End def -----------------------------------------------------
        
    def Btn_Event_Create_fkt_mask(self,ADummy): # Erstellt die Eingabemaske der Funktion
        if self.FEnableDebugPrint:
            print("Debug: Btn_Event_Create_fkt_mask  ")    
        
        
               
        
        
        if self.FxWerteAlsInit:
            self.Ftxt_All_Input.value = self.RS_Symbol_fue_X_Werte
            self.FCurrentValue = self.FxWerte
        else:
            self.Ftxt_All_Input.value = str(self.FFloat_Init_Fkt.value)  
            self.FCurrentValue = self.FFloat_Init_Fkt.value  
        

        self.FListClass_btn_Menu = self.FListClass_btn_Menu + [ 
            Class_btn_Menu(self.FxWerte,self.FCurrentValue,self.Ftxt_All_Input,False,None,None,self.New_Tab,self.Delete_Tab,0) 
            ]
        self.FTabItems = self.FTabItems + [self.FListClass_btn_Menu[0].btn_BTNMenu_erstellen(False)]
        self.FTab = Tab(self.FTabItems)   
        self.FTab.set_title(0, self.RS_Tab_Titel_Main) 
        
        all_box_items = [self.Ftxt_All_Input , self.FTab]
        all_box = VBox(children=all_box_items)    
    
        form_fkt_mask_items = [all_box]   

        form_fkt_mask = Box(form_fkt_mask_items , layout=self.F_wdg_Box_Layout)            
        self.FMaskResultIteams = form_fkt_mask_items
        self.FMaskResultForm = form_fkt_mask
        if len(self.FAccItems) > 2:
            self.FAccItems[2].close 
            self.FAccItems.pop(2)
        self.FAccItems = self.FAccItems + [ form_fkt_mask ]
        self.FAcc.children = self.FAccItems 
        self.FAcc.selected_index = len(self.FAccItems)-1
# ---------------------------------------------------- End def -----------------------------------------------------   
    def Btn_Event_x_Werte_einfuegen(self,ADummy):  
        self.FxWerteAlsInit = True
        self.Btn_Event_Create_fkt_mask(None)
# ---------------------------------------------------- End def -----------------------------------------------------    
    def Btn_Event_Init_Input_Fkt(self,ADummy):
        if self.FEnableDebugPrint:
            print('Debug: Init Input Fkt') 
            
        btn_Weiter =  Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Btn_Weiter)
        btn_Weiter.on_click(self.Btn_Event_Create_fkt_mask)
        
        btn_x_Werte_einfuegen = Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Btn_Use_x_Values)
        btn_x_Werte_einfuegen.on_click(self.Btn_Event_x_Werte_einfuegen)
      
        fs = self.FFloat_Abtastfrequenz.value 
        self.FxWerte = np.arange(-10,10+1/fs,1/fs)
        
        InitSubHBoxItems = [btn_Weiter,btn_x_Werte_einfuegen]
        InitSubHBox = HBox(InitSubHBoxItems)
        InitHBoxItems =[ self.FFloat_Init_Fkt ,
                     Text(layout= self.F_wdg_Layout, value=self.RS_x_Array, disabled=True),
                     Text(layout= self.F_wdg_Layout, value=str(self.FxWerte), disabled=True),
                     InitSubHBox 
                   ]
        
        InitHBox = HBox(children=InitHBoxItems, layout=self.F_wdg_Box_Layout)
      
        if len(self.FAccItems) > 1:
            self.FAccItems[1].close 
            self.FAccItems.pop(1)
        self.FAccItems = [self.FAccItems[0]] + [ InitHBox ]
        self.FAcc.children = self.FAccItems
        self.FAcc.selected_index = len(self.FAccItems)-1
# ---------------------------------------------------- End def -----------------------------------------------------        
    
    
        
    def Create(self,ADummy): # Erstellt die Eingabemöglichkeit für die Anzahl der SubFunktionen
       
        b = Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Btn_Eingabemaske_erzeugen)
        b.on_click(self.Btn_Event_Init_Input_Fkt)

        form_fkt_items = [
                Text(layout=self.F_wdg_Layout, value=self.RS_Abtastfrequenz, disabled=True),

                 self.FFloat_Abtastfrequenz,   


                Text(layout= self.F_wdg_Layout, value=self.RS_Titel_Typ_Funktion, disabled=True),

                Dropdown(options=[self.RS_Dpd_Reelle_Funktion, '', ''],value=self.RS_Dpd_Reelle_Funktion,description=self.RS_Funktion,disabled=False,
                         button_style='' # 'success', 'info', 'warning', 'danger' or ''
                        ),

                 b,
        ] 
        

        form_new_fkt = Box(form_fkt_items, layout=self.F_wdg_Box_Layout)
        if len(self.FAccItems) > 0:
            self.FAccItems[0].close
        self.FAccItems = [form_new_fkt]
        self.FAcc = Accordion(children=self.FAccItems)
        self.FAcc.set_title(0, self.RS_Acc_Titel_Setup)
        self.FAcc.set_title(1, 'Eingabe Startwert')    
        self.FAcc.set_title(2, self.RS_Acc_Titel_Mask) 
        self.FAcc.set_title(3, 'Plot') 
        display(self.FAcc)
        return self.RS_Help_Setup_Funktion     
# ---------------------------------------------------- End def -----------------------------------------------------        
  
    

              


# In[40]:

# New_Fkt = Class_Create_New_Function()
# Help=New_Fkt.Create_fkt_layout(None)

