
# coding: utf-8

from __future__ import print_function

from IPython.display import display

from ipywidgets import Accordion
from ipywidgets import Layout
from ipywidgets import Box
from ipywidgets import VBox
from ipywidgets import HBox
from ipywidgets import Button
from ipywidgets import Text

#from ipywidgets import Dropdown

from ipywidgets import FloatText
from ipywidgets import Tab

from . import signalgen as sig
import numpy as np


class Class_btn_Menu (object) :

    def __init__(self,AIsDiscret,AxValues,AFrequenz, ACurrentSignal ,ACurrentValue,Atxt_All_Input,AIsSub,AForwardOperator,AForwardFkt, ADefNewTab, ADefDeleteTab, ASubCount):
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
        self.RS_Help_Class = 'Gibt mittels "btn_BTNMenu_erstellen" das Button-Menu zur Eingabe von Funktionen zurück'
        # Texte
        self.RS_Funktion='Funktion:'
        self.RS_Amplitude='Amplitude'
        self.RS_Anzahl='Anzahl:'
        self.RS_Nichts = ''
        self.RS_Titel_Setup_Funktion = 'Anzahl der Teil-Funktionen und Operatoren'
        self.RS_Titel_Typ_Funktion = 'Typ der Funktion'
        self.RS_Titel_Mask_Funktion = 'Eingabe der Funktion: Hinweis Variable mit "x" eintragen'
        self.RS_Zahl = 'Zahl'
        self.RS_Symbol_fue_X_Werte = 't'
        self.RS_Symbol_fue_Frequenz = 'f'
        self.RS_Symbol_fue_Pi = 'PI'
        self.RS_Plus = '+'
        self.RS_Minus = '-'
        self.RS_Mul = '*'
        self.RS_Div = '/'
        self.RS_Sin = 'Sin('
        self.RS_Cos = 'Cos('
        self.RS_Klammer_auf = '('
        self.RS_Klammer_zu =')'
        # ====================================== Definition "def" übergreifende Variablen ======================================
        self.FIsDiscret = AIsDiscret
        self.FxWerte = AxValues
        self.FFrequenz = AFrequenz
        self.FNutzeXWerte = False
        self.FNutzeFrequenz = False
        self.FInputContCos = False
        self.FInputContSin = False
        self.FNutzePi = False
        self.FBefehl = None
        self.FInputA = None
        self.FInputB = None
        self.FIsSub  = AIsSub
        self.FSubFirstNum = True
        self.FCurrentValue = ACurrentValue
        self.FSubCurrentValue = None

        self.FCurrentSignal = ACurrentSignal
        self.FSubCurrentSignal = None


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

        if self.FIsDiscret:
            self.Fbtn_Num = Button(layout=self.F_wdg_Layout,button_style='warning',description='Zahl')
        else:
            self.Fbtn_Num = Button(layout=self.F_wdg_Layout,button_style='warning',description='Konstante')
        self.Fbtn_Cos = Button(layout=self.F_wdg_Layout,button_style='warning',description='Cos')

        self.Fbtn_Sin = Button(layout=self.F_wdg_Layout,button_style='warning',description='Sin')

        self.Fbtn_Klammer = Button(layout=self.F_wdg_Layout,button_style='warning',description='Klammer')

        self.Fbtn_Frequenz_Einfuegen = Button(layout=self.F_wdg_Layout,button_style='warning',description='Frequenz')

        self.Fbtn_Pi_Einfuegen = Button(layout=self.F_wdg_Layout,button_style='warning',description='Pi')

        self.Fbtn_Eingeben = Button(layout=self.F_wdg_Layout,button_style='warning',description='Weiter')

        if self.FIsSub:
            self.Fbtn_KlammerZu = Button(layout=self.F_wdg_Layout,button_style='warning',description='Klammer schließen')
        else:
            self.Fbtn_KlammerZu = Button(layout=self.F_wdg_Layout,button_style='warning',description='Fertig')

        self.Fbtn_x_Werte_Einfuegen = Button(layout=self.F_wdg_Layout,button_style='warning',description='x-Werte einfügen')

        if self.FIsDiscret:
            self.Ftxt_Num = FloatText(Layout=self.F_wdg_Layout,value=1, description=self.RS_Zahl, disabled=False)
        else:
            self.Ftxt_Num = FloatText(Layout=self.F_wdg_Layout,value=1, description=self.RS_Amplitude, disabled=False)



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
                if self.FIsDiscret:
                    self.FSubCurrentValue = np.add(self.FInputA,self.FInputB)
                else:
                    del self.FSubCurrentSignal
                    self.FSubCurrentSignal = sig.add(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentSignal))
            else:
                if self.FIsDiscret:
                    self.FCurrentValue = np.add(self.FInputA,self.FInputB)

                else:
                    del self.FCurrentSignal
                    self.FCurrentSignal = sig.add(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentVSignal))



        if self.FBefehl == self.RS_Minus :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Minus')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) )
            if self.FIsSub:
                if self.FIsDiscret:
                    self.FSubCurrentValue = np.subtract(self.FInputA,self.FInputB)
                else:
                    del self.FSubCurrentSignal
                    self.FSubCurrentSignal = sig.sub(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentSignal))
            else:
                if self.FIsDiscret:
                    self.FCurrentValue = np.subtract(self.FInputA,self.FInputB)
                else:
                    del self.FCurrentSignal
                    self.FCurrentSignal = sig.sub(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentVSignal))



        if self.FBefehl == self.RS_Mul :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case mul')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) )
            if self.FIsSub:
                if self.FIsDiscret:
                    self.FSubCurrentValue = np.multiply(self.FInputA,self.FInputB)
                else:
                    del self.FSubCurrentSignal
                    self.FSubCurrentSignal = sig.mul(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentSignal))
            else:
                if self.FIsDiscret:
                    self.FCurrentValue = np. multiply(self.FInputA,self.FInputB)
                else:
                    del self.FCurrentSignal
                    self.FCurrentSignal = sig.mul(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentVSignal))

        if self.FBefehl == self.RS_Div :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case div')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) )
            if self.FIsSub:
                if self.FIsDiscret:
                    self.FSubCurrentValue = np.divide(self.FInputA,self.FInputB)
                else:
                    del self.FSubCurrentSignal
                    self.FSubCurrentSignal = sig.div(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentSignal))
            else:
                if self.FIsDiscret:
                    self.FCurrentValue = np.divide(self.FInputA,self.FInputB)
                else:
                    del self.FCurrentSignal
                    self.FCurrentSignal = sig.div(self.FInputA,self.FInputB)
                    del self.FInputA
                    del self.FInputB
                    self.FInputA = None
                    self.FInputB = None

                if self.FEnableDebugPrint:
                    print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentVSignal))



        if self.FBefehl == self.RS_Cos :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Cos')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) )
            if self.FIsSub:
                if self.FIsDiscret:
                    self.FSubCurrentValue = np.cos(self.FInputB)
                    if self.FEnableDebugPrint:
                        print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue))
            else:
                if self.FIsDiscret:
                    self.FCurrentValue = np.cos(self.FInputA,self.FInputB)
                    if self.FEnableDebugPrint:
                        print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'CurrentValue: ' + str(self.FCurrentValue))



        if self.FBefehl == self.RS_Sin :
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: Case Sin')
                print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'Sub: InputA: ' + str(self.FInputA) + ' InputB: ' + str(self.FInputB) )
            if self.FIsSub:
                if self.FIsDiscret:
                    self.FSubCurrentValue = np.sin(self.FInputB)
                    if self.FEnableDebugPrint:
                        print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue))
            else:
                if self.FIsDiscret:
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
#                 self.FSubCurrentValue = self.FInputB
                self.FSubCurrentSignal = self.FInputB
# ---------------------------------------------------- End def -----------------------------------------------------
    def KlammerSchließen(self,ADummy):
#         if self.FIsDiscret:

#             if self.FNutzeXWerte:
#                     self.FInputB = self.FxWerte
#                     self.FNutzeXWerte = False
#                 elif self.FNutzeFrequenz:
#                     self.FInputB = self.FFrequenz
#                     self.FNutzeFrequenz = False
#                 elif self.FNutzePi:
#                     self.FInputB = np.pi
#                     self.FNutzePi = False
#                 else:
#                     self.FInputB = self.Ftxt_Num.value

#             self.FInputB = self.Ftxt_Num.value
#         else:
#             self.FInputB = sig.const(self.Ftxt_Num.value)  # cos und so noch

#         if self.FIsSub :
#             if self.FIsDiscret:
#                 self.FInputA = self.FSubCurrentValue
#             else:
#                 self.FInputA = self.FSubCurrentSignal

#
        if self.FIsSub:


            if self.FIsDiscret:
                self.FInputA = self.FCurrentValue
                self.FInputB = self.FSubCurrentValue

            else:
                self.FInputA = self.FCurrentSignal
                self.FInputB = self.FSubCurrentSignal

            self.FBefehl = self.FForwardFkt # erst ggf. Cos, Sin usw. ausrechnen dan +,- ... z.b ..+Cos()

            self.Switch_Case_für_Numpy(None)

            if self.FIsDiscret:
                self.FInputA = self.FCurrentValue
                self.FInputB = self.FSubCurrentValue
            else:
                self.FInputA = self.FCurrentSignal
                self.FInputB = self.FSubCurrentSignal

            self.FBefehl = self.FForwardOperator # anschließen das +,- usw rechnen
            self.Switch_Case_für_Numpy(None)

            if self.FIsDiscret:
                    self.FCurrentValue = self.FSubCurrentValue
            else:
                    self.FCurrentSignal= self.FSubCurrentSignal
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
        self.Fbtn_Frequenz_Einfuegen.disabled   = True
        self.Fbtn_Pi_Einfuegen.disabled   = True
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

#         if self.FIsSub :
#             if self.FSubFirstNum :
#                 self.FSubFirstNum = False
#                 if self.FIsDiscret:
#                     self.FSubCurrentValue = self.Ftxt_Num.value
#                 else:
#                     self.FSubCurrentValue = sig.const(self.Ftxt_Num.value)
#                 if self.FEnableDebugPrint:
#                     print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + 'SubCurrentValue: ' + str(self.FSubCurrentValue))
        self.Ftxt_Num.disabled  = False
        self.Fbtn_Eingeben.disabled  = False
        self.Fbtn_x_Werte_Einfuegen.disabled  = False
        self.Fbtn_Frequenz_Einfuegen.disabled   = False
        self.Fbtn_Pi_Einfuegen.disabled   = False
# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_Sin(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Sin)

        if self.FIsDiscret:
            self.disable_btn(None)
            self.FBefehl = self.RS_Sin
            self.FFkt=self.RS_Sin
            self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Sin
            if self.FIsSub :
                self.FDefNewTab(self.FOperator,self.FFkt,self.FSubCurrentValue,self.FSubCurrentSignal)
            else:
                self.FDefNewTab(self.FOperator,self.FFkt,self.FCurrentValue,self.FCurrentSignal)
        else:
            self.FInputContSin = True
            self.Fbtn_Eingeben.disabled  = False
            self.Fbtn_x_Werte_Einfuegen.disabled  = False
            self.Fbtn_Frequenz_Einfuegen.disabled   = False
            self.Fbtn_Pi_Einfuegen.disabled   = False
            self.Ftxt_Num.disabled  = False
# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_Cos(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Cos)

        if self.FIsDiscret:
            self.disable_btn(None)
   #         alterBefehl = self.FBefehl
            self.FBefehl = self.RS_Cos
            self.FFkt=self.RS_Cos
            self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Cos
            if self.FIsSub :
                self.FDefNewTab(self.FOperator,self.FFkt,self.FSubCurrentValue,self.FSubCurrentSignal)
            else:
                self.FDefNewTab(self.FOperator,self.FFkt,self.FCurrentValue,self.FCurrentSignal)
        else:
            self.FInputContCos = True
            self.Fbtn_Eingeben.disabled  = False
            self.Fbtn_x_Werte_Einfuegen.disabled  = False
            self.Fbtn_Frequenz_Einfuegen.disabled   = False
            self.Fbtn_Pi_Einfuegen.disabled   = False
            self.Ftxt_Num.disabled  = False



# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_Klammer_auf(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +'Debug: ' + self.RS_Klammer_auf)
        self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Klammer_auf
      #  alterBefehl = self.FBefehl
        self.FBefehl = self.RS_Klammer_auf
        self.disable_btn(None)
        self.FFkt=self.RS_Klammer_auf
        if self.FIsSub :
            self.FDefNewTab(self.FOperator,self.FFkt,self.FSubCurrentValue,self.FSubCurrentSignal)
        else:
            self.FDefNewTab(self.FOperator,self.FFkt,self.FCurrentValue,self.FCurrentSignal)

# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_Weiter(self,ADummy):
        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount+ ':' +'Debug: btn_Event_Weiter')
        self.Fbtn_KlammerZu.disabled  = False





        if self.FNutzeXWerte:
            Value = self.FxWerte
            self.FNutzeXWerte = False
            if self.FIsDiscret:
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Symbol_fue_X_Werte
            else:
                SymValue =  self.RS_Symbol_fue_X_Werte

        elif self.FNutzeFrequenz:
            Value  = self.FFrequenz
            self.FNutzeFrequenz = False
            if self.FIsDiscret:
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Symbol_fue_Frequenz
            else:
                SymValue =  self.RS_Symbol_fue_Frequenz
        elif self.FNutzePi:
            Value = np.pi
            self.FNutzePi = False
            if self.FIsDiscret:
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Symbol_fue_Pi
            else:
                SymValue =  self.RS_Symbol_fue_Pi
        else:
            Value = self.Ftxt_Num.value
            if self.FIsDiscret:
                self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + str(self.Ftxt_Num.value )
            else:
                SymValue =  str(self.Ftxt_Num.value )


        if self.FIsSub :
            self.Enable_left_btn(None)
            if self.FIsDiscret:
                self.FInputA = self.FSubCurrentValue
                if self.FSubFirstNum:
                    self.FSubFirstNum = False
                    self.FSubCurrentValue = Value
                else:
                    self.FInputB = Value
            else:
                self.FInputA = self.FSubCurrentSignal
                if self.FInputContCos:
                    self.FInputContCos = False
                    self.FInputB = sig.sine(self.FFrequenz, Value)
                    self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Sin+'f,'+SymValue+')'
                elif self.FInputContSin:
                    self.FInputContSin = False
                    self.FInputB = sig.cosine(self.FFrequenz, Value)
                    self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Sin+'f,'+SymValue+')'

                else:
                    self.FInputB = sig.const(Value)
                    self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + SymValue



        else:
            if self.FIsDiscret:
                self.FInputA = self.FCurrentValue
                self.FInputB = Value

            else:
                self.FInputA = self.FCurrentSignal
                if self.FInputContCos:
                    self.FInputContCos = False
                    self.FInputB = sig.cosine(self.FFrequenz,str(Value))
                    self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Cos+'f,'+SymValue+')'
                elif self.FInputContSin:
                    self.FInputContSin = False
                    self.FInputB = sig.cosine(self.FFrequenz,str(Value))
                    self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + self.RS_Sin+'f,'+SymValue+')'
                else:
                    self.FInputB = sig.const(Value)
                    self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + SymValue


        self.Switch_Case_für_Numpy(None)


        self.Enable_left_btn(None)
        self.Fbtn_Eingeben.disabled  = True
        self.Fbtn_x_Werte_Einfuegen.disabled   = True
        self.Fbtn_Frequenz_Einfuegen.disabled   = True
        self.Fbtn_Pi_Einfuegen.disabled   = True
#             self.FDefDeleteTab(None)
# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_x_Werte_einfuegen(self,ADummy):
        self.FNutzeXWerte = True
        self.btn_Event_Weiter(None)
        self.Fbtn_Eingeben.disabled  = True
        self.Fbtn_x_Werte_Einfuegen.disabled   = True
        self.Fbtn_Frequenz_Einfuegen.disabled   = True
        self.Fbtn_Pi_Einfuegen.disabled   = True
    def btn_Event_Frequenz_einfuegen(self,ADummy):
        self.FNutzeFrequenz = True
        self.btn_Event_Weiter(None)
        self.Fbtn_Eingeben.disabled  = True
        self.Fbtn_x_Werte_Einfuegen.disabled   = True
        self.Fbtn_Frequenz_Einfuegen.disabled   = True
        self.Fbtn_Pi_Einfuegen.disabled   = True

    def btn_Event_Pi_einfuegen(self,ADummy):
        self.FNutzePi = True
        self.btn_Event_Weiter(None)
        self.Fbtn_Eingeben.disabled  = True
        self.Fbtn_x_Werte_Einfuegen.disabled   = True
        self.Fbtn_Frequenz_Einfuegen.disabled   = True
        self.Fbtn_Pi_Einfuegen.disabled   = True

# ---------------------------------------------------- End def -----------------------------------------------------
    def btn_Event_Klammer_zu(self,ADummy):

        if self.FIsSub:
            self.KlammerSchließen(None);
            self.Ftxt_All_Input.value = self.Ftxt_All_Input.value + ')'
        else:
            if self.FEnableDebugPrint:
                print('Fenster Nr: ' + self.FSubCount+ ':' +'Debug: btn_Event_Klammer_zu')
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
        self.Fbtn_Sin.on_click( self.btn_Event_Sin )
        self.Fbtn_Num.on_click( self.btn_Event_Num )
        self.Fbtn_Klammer.on_click( self.btn_Event_Klammer_auf )

        self.Fbtn_Eingeben.on_click( self.btn_Event_Weiter )
        self.Fbtn_KlammerZu.on_click( self.btn_Event_Klammer_zu )
        self.Fbtn_x_Werte_Einfuegen.on_click(self.btn_Event_x_Werte_einfuegen)
        self.Fbtn_Frequenz_Einfuegen.on_click(self.btn_Event_Frequenz_einfuegen)
        self.Fbtn_Pi_Einfuegen.on_click(self.btn_Event_Pi_einfuegen)

        self.disable_btn(None)
        self.Enable_left_btn(None)
        self.Fbtn_KlammerZu.disabled  = False

        if ADisable_btn_left == True :
            self.disable_btn(None)
            self.Enable_btn(None)
            self.Fbtn_Eingeben.disabled  = True
            self.Fbtn_Frequenz = Button(layout=self.F_wdg_Layout,button_style='warning',description='Frequenz')



        btn_links = [ self.Fbtn_Add, self.Fbtn_Sub, self.Fbtn_Mul, self.Fbtn_Div]
        btn_rechts = [ self.Fbtn_Num, self.Fbtn_Cos, self.Fbtn_Sin, self.Fbtn_Klammer]
        if self.FIsDiscret :
            btn_const =  [self.Fbtn_x_Werte_Einfuegen,self.Fbtn_Frequenz_Einfuegen,self.Fbtn_Pi_Einfuegen]
        else:
            btn_const =  [self.Fbtn_Frequenz_Einfuegen,self.Fbtn_Pi_Einfuegen]

        itm_rechts = [ self.Ftxt_Num, self.Fbtn_Eingeben]

      #  btn_SubHBox1 = HBox(children=[])

      #  btn_SubHBox2 = HBox(children=[ self.Fbtn_Eingeben])
        


        
        btn_VBoxr = VBox(children=btn_rechts)
        btn_VBoxl = VBox(children=btn_links)
        btn_VBoxconst = VBox(children=btn_const)
        itm_VBoxr = VBox(children=itm_rechts)


        HBoxItems = [ btn_VBoxl,btn_VBoxr, btn_VBoxconst,itm_VBoxr,self.Fbtn_KlammerZu ]
        btn_HBox = HBox(children=HBoxItems)

        if self.FEnableDebugPrint:
            print('Fenster Nr: ' + self.FSubCount +':' +"Debug: btn_Tab")



        return btn_HBox


# ************************************************************************************************************************************************************************************
#               Class ENDE                                Class ENDE                                Class ENDE
# ************************************************************************************************************************************************************************************




class Class_Create_New_Function(object) :

    def __init__(self,AIsDiscret):
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
        self.RS_Titel_Setup_Funktion = 'Anzahl der Teilfunktionen und Operatoren'
        self.RS_Titel_Typ_Funktion = 'Typ der Funktion'
        self.RS_Titel_Mask_Funktion = 'Eingabe der Funktion: Hinweis Variable mit "x" eintragen'
        self.RS_x_Werte_einfuegen = 'x-Werte einfügen'
        self.RS_Zahl = 'Zahl'
        self.RS_Abtastfrequenz = 'Abtastfrequenz in Hz'
        self.RS_x_Array = 'Array der X-Werte'
        self.RS_Frequenz = 'Signalfrequnz'
        # Help Texte
        self.RS_Help_Class = 'Erzeugt mittels "Create_fkt_layout" die Eingabemaske zum erzeugen einer neuen Funktion'
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
        self.RS_x_Min = 'x Minimum'
        self.RS_x_Max = 'x Maximum'
        # ====================================== Definition "def" übergreifende Variablen ======================================
        self.FIsDiscret = AIsDiscret
        self.FMaskResultIteams = None
        self.FMaskResultForm = None
        self.FCurrentValue = None
        self.FSubCurrentValue = None

        self.FCurrentSignal = None
        self.FSubCurrentSignal = None
        self.FResultSignal = None

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

        self.FFloat_Frequenz =FloatText(layout=self.F_wdg_Layout,value=10, disabled=False)
        
        
        self.FFloat_x_Min = FloatText(layout=self.F_wdg_Layout,value=-10, disabled=False,  )
       
        self.FFloat_x_Max = FloatText(layout=self.F_wdg_Layout,value=10, disabled=False)

        self.Ftxt_All_Input = Text(layout=self.F_wdg_Layout, value='Eingegebene Formel', disabled=True)

        self.Ftxt_Current_Input = Text(layout=self.F_wdg_Layout, value='Aktuelle Eingabe', disabled=False)

        self.FFloat_Init_Fkt = FloatText(Layout=self.F_wdg_Layout,value=1, description=self.RS_Zahl, disabled=False)

        self.FTabItems = []

        self.FTab = None
        
        self.Fbtn_Weiter_Create = Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Btn_Eingabemaske_erzeugen)
       
        self.Fbtn_Weiter_Init =  Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Btn_Weiter)
     
        self.Fbtn_x_Werte_einfuegen = Button(layout=self.F_wdg_Layout,button_style='warning',description=self.RS_Btn_Use_x_Values)
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

            if self.FIsDiscret:
                self.FCurrentValue = self.FListClass_btn_Menu[i].FCurrentValue
            else:
                self.FCurrentSignal = self.FListClass_btn_Menu[i].FCurrentSignal

            if len(self.FListClass_btn_Menu) > 2 :
                if self.FIsDiscret:
                    self.FListClass_btn_Menu[i-1].FSubCurrentValue  = self.FListClass_btn_Menu[i].FSubCurrentValue
                else:
                    self.FListClass_btn_Menu[i-1].FSubCurrentSignal  = self.FListClass_btn_Menu[i].FSubCurrentSignal
#

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
            self.Fertig(None)
# ---------------------------------------------------- End def -----------------------------------------------------

    def New_Tab(self,AForwardOperator,AForwardFkt,ACurrentValue,ACurrentSignal):
        if self.FEnableDebugPrint:
            print('Debug: Neues Tab')
        i = len(self.FListClass_btn_Menu)
        self.FListClass_btn_Menu = self.FListClass_btn_Menu + [ Class_btn_Menu(
                self.FIsDiscret,
                self.FxWerte,
                self.FFrequenz,
                ACurrentSignal,
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
    def Fertig(self,ADummy):
        if self.FEnableDebugPrint:
            print('Debug: def Fertig')


        if self.FIsDiscret:
            if self.FListClass_btn_Menu[0].FFkt == None:
                self.FCurrentValue = self.FListClass_btn_Menu[0].FCurrentValue

         #   print('self.FListClass_btn_Menu[0].FFkt             ' + str(self.FListClass_btn_Menu[0].FFkt))
         #   print('self.FListClass_btn_Menu[0].FCurrentValue    ' + str(self.FListClass_btn_Menu[0].FCurrentValue))
         #   print('self.FListClass_btn_Menu[0].FSubCurrentValue ' + str(self.FListClass_btn_Menu[0].FSubCurrentValue))
         #   print('self.FCurrentValue                           ' + str(self.FCurrentValue))
         #   print('self.FSubCurrentValue                        ' + str(self.FSubCurrentValue))
            
            if isinstance(self.FCurrentValue , float) :
                self.FCurrentValue = [self.FCurrentValue for i in range(len(self.FxWerte))]

            self.FyWerte = self.FCurrentValue



        else:
            if self.FListClass_btn_Menu[0].FFkt == None:
                self.FCurrentSignal = self.FListClass_btn_Menu[0].FCurrentSignal
            self.FResultSignal = self.FCurrentSignal

        self.FTab.visible = False
        #self.FAcc.visible = False  # Leider ist es nicht möglich das widget "ordentlich" zu löschen,
                                    # daher nur unsichtbar gemacht
                                    # löschen ist aber "per Hand" mit dem klein x links neben den wdg möglich

# ---------------------------------------------------- End def -----------------------------------------------------

    def Btn_Event_Create_fkt_mask(self,ADummy): # Erstellt die Eingabemaske der Funktion
        if self.FEnableDebugPrint:
            print("Debug: Btn_Event_Create_fkt_mask  ")

        if self.FIsDiscret:
            if self.FxWerteAlsInit:
                self.Ftxt_All_Input.value = self.RS_Symbol_fue_X_Werte
                self.FCurrentValue = self.FxWerte
            else:
                self.Ftxt_All_Input.value = str(self.FFloat_Init_Fkt.value)
                self.FCurrentValue = self.FFloat_Init_Fkt.value

        else:
             self.Ftxt_All_Input.value = str(self.FFloat_Init_Fkt.value)
             self.FCurrentSignal = sig.const(self.FFloat_Init_Fkt.value)

        # "Main-Taschenrechner"-Tab erzeugen, alle zusätzlichen sub-Tabs über die def New_Tab
        self.FListClass_btn_Menu = self.FListClass_btn_Menu +  [

                                        Class_btn_Menu(self.FIsDiscret,
                                                       self.FxWerte,
                                                       self.FFrequenz,
                                                       self.FCurrentSignal,
                                                       self.FCurrentValue,
                                                       self.Ftxt_All_Input,
                                                       False,
                                                       None,
                                                       None,
                                                       self.New_Tab,
                                                       self.Delete_Tab,0)
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

        if len(self.FAccItems) > 1:
            self.FAccItems[1].close
            self.FAccItems.pop(1)

        self.FAccItems = self.FAccItems + [ form_fkt_mask ]
        self.FAcc.children = self.FAccItems
        self.FAcc.selected_index = len(self.FAccItems)-1
        self.FAcc.set_title(1, self.RS_Acc_Titel_Mask)
        
        self.Fbtn_x_Werte_einfuegen.disabled = True
        self.Fbtn_Weiter_Init.disabled = True
        self.FFloat_Init_Fkt.disabled = True

        print(('Hinweis: Leider ist es relativ kompliziert auch "Punkt vor Strich" zu beachten.'
               'Daher einfach Punktrechnungen in Klammern setzen'))
# ---------------------------------------------------- End def -----------------------------------------------------
    def Btn_Event_x_Werte_einfuegen(self,ADummy):
        if self.FIsDiscret:
            self.FxWerteAlsInit = True
            self.Btn_Event_Create_fkt_mask(None)
# ---------------------------------------------------- End def -----------------------------------------------------
    def Btn_Event_Init_Input_Fkt(self,ADummy):
        if self.FEnableDebugPrint:
            print('Debug: Init Input Fkt')

        
        self.Fbtn_Weiter_Init.on_click(self.Btn_Event_Create_fkt_mask)
        self.FFrequenz = self.FFloat_Frequenz.value
        if self.FIsDiscret:
            
            self.Fbtn_x_Werte_einfuegen.on_click(self.Btn_Event_x_Werte_einfuegen)
            fs = self.FFloat_Abtastfrequenz.value
            
            
            if self.FIsDiscret:                        
                self.FxWerte = np.arange(self.FFloat_x_Min.value,self.FFloat_x_Max.value+1/fs,1/fs)

            InitSubHBoxItems = [self.Fbtn_Weiter_Init, self.Fbtn_x_Werte_einfuegen]
        else:
            InitSubHBoxItems = [self.Fbtn_Weiter_Init]

        InitSubHBox = HBox(InitSubHBoxItems)


        if self.FIsDiscret:
            InitHBoxItems = [ self.FFloat_Init_Fkt ,
                              Text(layout= self.F_wdg_Layout, value=self.RS_x_Array, disabled=True),
                              Text(layout= self.F_wdg_Layout, value=str(self.FxWerte), disabled=True),
                              InitSubHBox
                            ]
        else:
             InitHBoxItems = [ self.FFloat_Init_Fkt ,  InitSubHBox ]


        InitHBox = HBox(children=InitHBoxItems, layout=self.F_wdg_Box_Layout)

        if len(self.FAccItems) > 1:
            self.FAccItems[1].close
            self.FAccItems.pop(1)
            

        self.FAccItems = [self.FAccItems[0]] + [ InitHBox ]
        self.FAcc.children = self.FAccItems
        self.FAcc.selected_index = len(self.FAccItems)-1


        self.Fbtn_Weiter_Create.disabled = True
        if self.FIsDiscret: 
            self.FFloat_Abtastfrequenz.disabled = True
        self.FFloat_Frequenz.disabled = True
        
    # ---------------------------------------------------- End def -----------------------------------------------------



    def Create(self,AIsDiscrete): # Erstellt die Eingabemöglichkeit für die Anzahl der SubFunktionen

        # Butten um zum nächsten "Tab" zu gehen und Eingaben zu übernehemen
        
        self.Fbtn_Weiter_Create.on_click(self.Btn_Event_Init_Input_Fkt)

        # Liste der Eingabe-Widgets, wenn diskret zusätzlich Abtastfrequenz eingeben
        if self.FIsDiscret:
            Box_Fkt_Items = [
                                Text(layout=self.F_wdg_Layout, value=self.RS_Abtastfrequenz, disabled=True, visible = True),
                                 self.FFloat_Abtastfrequenz,
                                 Text(layout=self.F_wdg_Layout, value=self.RS_Frequenz, disabled=True, visible = True),
                                 self.FFloat_Frequenz,
                #                 Text(layout= self.F_wdg_Layout, value=self.RS_Titel_Typ_Funktion, disabled=True),
                #                 Dropdown(options=[self.RS_Dpd_Reelle_Funktion, '', ''],value=self.RS_Dpd_Reelle_Funktion,description=self.RS_Funktion,disabled=False,
                #                          button_style='' # 'success', 'info', 'warning', 'danger' or ''
                #                         ),
                
                                           
                                 Text(layout=self.F_wdg_Layout, value=self.RS_x_Min, disabled=True, visible = True)  ,        
                                 self.FFloat_x_Min,
                                 Text(layout=self.F_wdg_Layout, value=self.RS_x_Max, disabled=True, visible = True)  , 
                                 self.FFloat_x_Max,
                                 self.Fbtn_Weiter_Create
                            ]
        else:
            Box_Fkt_Items = [    Text(layout=self.F_wdg_Layout, value=self.RS_Frequenz, disabled=True, visible = True),
                                 self.FFloat_Frequenz,
                #                 Text(layout= self.F_wdg_Layout, value=self.RS_Titel_Typ_Funktion, disabled=True),
                #                 Dropdown(options=[self.RS_Dpd_Reelle_Funktion, '', ''],value=self.RS_Dpd_Reelle_Funktion,description=self.RS_Funktion,disabled=False,
                #                          button_style='' # 'success', 'info', 'warning', 'danger' or ''
                #                         ),
                                 self.Fbtn_Weiter_Create
                            ]
            self.FFloat_Abtastfrequenz = None


        Box_New_Fkt = Box(Box_Fkt_Items, layout=self.F_wdg_Box_Layout)
        if len(self.FAccItems) > 0: # wenn neu erzeugt wird altes Fenster Löschen
            self.FAccItems[0].close

        self.FAccItems = [Box_New_Fkt]
        self.FAcc = Accordion(children=self.FAccItems)
        self.FAcc.set_title(0, self.RS_Acc_Titel_Setup)
        self.FAcc.set_title(1, 'Eingabe Startwert')


        display(self.FAcc)
        #return self.RS_Help_Setup_Funktion
# ---------------------------------------------------- End def -----------------------------------------------------


# ************************************************************************************************************************************************************************************
#               Class ENDE                                Class ENDE                                Class ENDE
# ************************************************************************************************************************************************************************************
