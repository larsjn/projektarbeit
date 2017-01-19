import lib.createcomplexsignal as kpl
import lib.createsignal as inp
import lib.plotwidget as sigplt
import numpy as np
import parser
import csv
from abc import ABCMeta, abstractmethod
from math import *

# Hinweise:
#   - übergabe Parameter wurden mit einem A vor dem Namen gekennzeichnet
#   - def übergreifende Variablen wurden zunächst alle in der Init vor definiert
#            o  def übergreifende Variablen wurden mit einem F vor dem Namen gekennzeichnet
#   - Texte die angezeigt werden wurden in der Init definiert und mit RS_ gekennzeichnet 
#            o  wenn Widget im Init definiert wurde ggf. der String direckt im Widget definiert

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                 BASIS KLASSEN
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Signal-Basisklasse - muss von allen Signal-Klassen implementiert werden
class signal(metaclass=ABCMeta):

    def __init__ (self, AType = None):
    # =============================================== verwendete Texte ===============================================
        self.RS_Typ_discrete        = "discrete"
        self.RS_Typ_continuous      = "continuous"
        self.RS_Typ_complex         = "complex"
        self.RS_ERROR_Listenlaenge  = 'ERROR: Länge der X und Y Listen unterscheiden sich. X-Liste zuerst setzten'

    # =============================================== def übergreifende Variablen ===============================================    
        self.FTyp       = AType
        self.FComplex   = None
        self.FComplex   = None
        self.FSignal    = None
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
#Operatorüberladungen für Rechenoperationen
    def __add__(self, other):
        return add(self, other)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    def __sub__(self, other):
        return sub(self, other)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    def __mul__(self, other):
        return mul(self, other)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    def __truediv__(self, other):
        return div(self, other)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Y-Wert an stelle X berechnen        
    def getYAt(selfe,Ax):
         pass
# ----------------------------------------------- ENDE DEF -----------------------------------------------     
    # X-Werte-Liste eines diskreten Signals falls vorhanden
    def getXList(self):
        return None
# ----------------------------------------------- ENDE DEF -----------------------------------------------         
    # Y-Werte an X Stellen berechnen -> Liste erzeugen
    def getList(self, AInList):
        # Je nach Signaltyp Funktionen ausführen
        if (self.FTyp == self.RS_Typ_discrete) or (self.FTyp == self.RS_Typ_continuous) :
            outList = [self.getYAt(x) for x in AInList]
            return outList
        elif self.FTyp == self.RS_Typ_complex:
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Konvertiert Komplexes-Eingabeformat zu Komplexem-Numpy-Format (True) oder behält Komplexes-Eingabeformat bei      
    def getZ(self,AAsNumpy=False):
        # Je nach Signaltyp Funktionen ausführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:  # Nur wenn eine komplexe Zahl definiert wurde
                if not AAsNumpy:
                    return self.FComplex.FZ
                else:
                    return np.array(self.FComplex.FZ)
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Realteil der komplexen Zahl zurück
    def getRe(self):
        # Je nach Signaltyp Funktionen ausführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:   # Nur wenn eine komplexe Zahl definiert wurde
               return self.FComplex.FRe
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird
# ----------------------------------------------- ENDE DEF -----------------------------------------------       
    # Gibt den Imaginärteil der komplexen Zahl zurück
    def getIm(self):
        # Je nach Signaltyp Funktionen ausführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:   # Nur wenn eine komplexe Zahl definiert wurde
               return self.FComplex.FIm
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Polaren-Winkel der komplexen Zahl zurück(Grad, oder Rad)
    def getAngle(self,ADegree = True):
        # Je nach Signaltyp Funktionen ausführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:   # Nur wenn eine komplexe Zahl definiert wurde
                if ADegree:
                    return self.FComplex.FAngle
                else:
                    return self.FComplex.FAngleRad
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Betrag der komplexen Zahl zurück
    def getAbs(self):
        # Je nach Signaltyp Funktionen ausführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:   # Nur wenn eine komplexe Zahl definiert wurde
                    return self.FComplex.FAbsolute
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Plottet Signale      
    def plot(self):
        sigplt.Class_Plot_Menu(self)
        return None 
# ----------------------------------------------- ENDE DEF -----------------------------------------------         
    # Updated Klassenvariablen 
    def update(self):
        pass
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  

# Basis-Klasse für kontinuierliche Signale
class contiuous(signal):
    # Gibt den y-Wert für einen gegebenen x-Wert zurück
    @abstractmethod
    def getYAt(self, x):
        pass
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  

# Basis-Klasse für diskrete Signale
class discrete(signal):
    pass
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                 SIGNALERZEUGUNG
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Nutzereingabe Parsen
class parseFkt(signal):
    def __init__(self, AFormula):
    # Initialisierung der Basisklasse
        super().__init__(None)
    # =============================================== def übergreifende Variablen =============================================== 
        # Parsen der Funktion
        self.FParserFunction = parser.expr(AFormula).compile()
        self.FTyp = self.RS_Typ_continuous

    def getYAt(self, time):
        t = time                    # Selbst bei Warnung, muss wegen Parser definiert werden
        return eval(self.FParserFunction) # Berechnen der Funktion für bestimmten Wert
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  

# Eine Signal per Bildungsvorschrift erzeugen
class create(signal):
    def __init__ (self, AType):
    # Initialisierung der Basisklasse
        super().__init__(AType)
    # =============================================== verwendete Texte ===============================================
        self.RS_Moegliche_Parameter = 'Mögliche Parameter:'
        self.RS_Warnung_1 = "Signal ist nicht kontinuierlich oder diskret"
    # =============================================== def übergreifende Variablen ===============================================   
        #Funktion als String (Parsereingabe zwischenspeicher)
        self.FInput = None

        #Erzeugen der Eingbaemaske je nach gewähltem Typ
        if AType == self.RS_Typ_continuous:
            self.FComplex = None
            self.FFunction = inp.Class_Input_Parser(True)
        elif AType == self.RS_Typ_discrete:
            self.FComplex = None
            self.FFunction = inp.Class_Input_Parser(False)
        elif AType == self.RS_Typ_complex:
            self.FFunction = None
            self.FComplex = kpl.create_complex()
        else:
            print(self.RS_Moegliche_Parameter + self.RS_Typ_discrete+","+self.RS_Typ_continuous+","+self.RS_Typ_complex)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    #Vorsorgliche Speicherfreigabe implementierung (unused)
    def delete_Values(self):
         # Je nach Signaltyp Funktionen ausführen
        if self.FTyp ==  self.RS_Typ_discrete:
            if self.FFunction != None:
                del self.FFunction
                self.FFunction = None
                return None
        elif self.FTyp == self.RS_Typ_continuous:
            return None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex != None:
                del self.FComplex
                self.FComplex = None
                return None
        else:
            return None 
        return None       
# ----------------------------------------------- ENDE DEF -----------------------------------------------  
    # Gibt den y-Wert für einen gegebenen x-Wert zurück  
    def getYAt(self,Ax): 
        # Je nach Signaltyp Funktionen ausführen
        if (self.FTyp ==  self.RS_Typ_discrete ) or (self.FTyp == self.RS_Typ_continuous):
            #Wenn sich die Eingabefunktion geändert hat: Neu parsen. Sonst bestehende Funktion verwenden
            if self.FFunction.FInput != self.FInput:
                self.parsedFktn = parseFkt(self.FFunction.FInput)
                self.FInput = self.FFunction.FInput
                return self.parsedFktn.getYAt(Ax)
            else:
                return self.parsedFktn.getYAt(Ax)
        elif self.FTyp == self.RS_Typ_complex:
            return None
        else:
            return None
        return None # Default Ausgabe wenn kein If erfüllt wird
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl        
    def __str__(self):
        # Je nach Signaltyp Funktionen ausführen
        if (self.FTyp ==  self.RS_Typ_discrete ) or (self.FTyp == self.RS_Typ_continuous):
            return self.FInput
        else:
            print(self.RS_Warnung_1)

        return None # Default Ausgabe wenn kein If erfüllt wird  
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
   # def getXList(self):
   #    if self.FFunction != None:
   #       self.update()
   #       return self.FxList
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


#                                  Kontinuierliche Signale - Klassendefinitonen 
#                                  Erweiterungsmöglichkeiten, z.B.: Dreieck oder Sägezahn Funktionsklassen

# Erzeugt Sinussignal 
class sine(contiuous):
    def __init__(self, AFrequency = 1, AAmplitude = 1):
    # Initialisierung der Basisklasse
        super().__init__("continuous")
    # =============================================== def übergreifende Variablen ===============================================    
        self.FFrequency = float(AFrequency)
        self.FAmplitude = float(AAmplitude)
        
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück  
    def getYAt(self, ATime):
        return self.FAmplitude * np.sin(2 * np.pi * self.FFrequency * ATime)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ermöglicht das setzen einer neuen Frequenz
    def setFreq(self, AFrequency):
        self.FFrequency = AFrequency
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ermöglicht das setzen einer neuen Amplitude
    def setAmp(self, AAmplitude):
        self.FAmplitude = AAmplitude
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    #def update(self):
    #    self.FFrequency = self.FFrequency
    #    self.FAmplitude = self.FAmplitude
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl 
    def __str__(self):
        return "{0}*sin(2*PI*{1}*t)".format(self.FAmplitude, self.FFrequency)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


# Erzeugt Cosinussignal 
class cosine(contiuous):
    def __init__(self, AFrequency = 1, AAmplitude = 1):
    # Initialisierung der Basisklasse
        super().__init__("continuous")
    # =============================================== def übergreifende Variablen ===============================================  
        self.FFrequency = float(AFrequency)
        self.FAmplitude = float(AAmplitude)

# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, ATime):
        return self.FAmplitude * np.cos(2.0 * np.pi * self.FFrequency * ATime)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ermöglicht das setzen einer neuen Frequenz
    def setFreq(self, AFrequency):
        self.FFrequency = AFrequency
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ermöglicht das setzen einer neuen Amplitude
    def setAmp(self, AAmplitude):
        self.FAmplitude = AAmplitude
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl 
    def __str__(self):
        return "{0}*cos(2*PI*{1}*t)".format(self.FAmplitude, self.FFrequency)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


# Erzeugt Squaresignal 
class square(contiuous):
    def __init__(self, AFrequency = 1, AAmplitude= 1, ADutyCycle = 0.5):
    # Initialisierung der Basisklasse
        super().__init__("continuous")
    # =============================================== def übergreifende Variablen ===============================================  
        self.FFrequency = AFrequency
        self.FAmplitude = AAmplitude
        self.FDutyCycle = ADutyCycle
        self.FTime      = 1 / self.FFrequency#
        self.FOnTime    = self.FTime * self.FDutyCycle
    # =============================================== nach init auszuführende def  ===============================================
        self.update()

# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, ATime):
        if((ATime % self.FTime) < self.FOnTime):
            return self.FAmplitude
        else: return - self.FAmplitude
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ermöglicht das setzen einer neuen Frequenz
    def setFreq(self, AFrequency):
        self.FFrequency = AFrequency
        self.update()
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ermöglicht das setzen einer neuen Amplitude
    def setAmp(self, AAmplitude):
        self.FAmplitude = AAmplitude
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ermöglicht das setzen eines neuen DutyCycle
    def setDutyCycle(self, ADutyCycle):
        self.FDutyCycle = ADutyCycle
        self.update()
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Berechnet Time neu für getYAt
    def update(self):
        self.FTime = 1 / self.FFrequency
        self.FOnTime = self.FTime * self.FDutyCycle
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


class const(contiuous):
    def __init__(self, AValue):
    # Initialisierung der Basisklasse
        super().__init__("continuous")
    # =============================================== def übergreifende Variablen ===============================================  
        self.FValue = AValue
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, Ax):
        return self.FValue
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    def setValue(self, AValue):
        self.FValue = AValue
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl 
    def __str__(self):
        return str(self.FValue)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


class contToDisc(signal):
    def __init__(self, ASignal, ASamplingRate=100, AStart=0, AEnd=10):
    # Initialisierung der Basisklasse
        super().__init__("discrete")
    # =============================================== def übergreifende Variablen ===============================================  
        self.FxList = np.arange(AStart, AEnd, 1 / ASamplingRate)
        self.FyList = ASignal.getList(self.FxList)
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Gibt eine Liste der X-Werte zurück
    def getXList(self):
        return self.FxList
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Gibt eine Liste der Y-Werte zurück
    def getYList(self):
        return self.FyList
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                                                 RECHENOPERRATIONEN
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Addieren zweier Signale gleichen Types
class add(signal):
    def __init__(self, ASignalA, ASignalB):
    # Initialisierung der Basisklasse
        super().__init__(ASignalA.FTyp )
    # =============================================== verwendete Texte ===============================================
        self.RS_Signal_A = 'Signal A'
        self.RS_Signal_B = 'Signal B'
        self.RS_Signal_AB = 'Signal A+B'
        self.RS_ERROR_1 = 'ERROR: Signaltypen unterscheiden sich'
    # =============================================== def übergreifende Variablen ===============================================  
        self.FsigA = ASignalA
        self.FsigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal A neu
    def setSigA(self, ASignalA):
        self.FsigA = ASignalA
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal B neu
    def setSigB(self, ASignalB):
        self.FsigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, ATime):
        # ggf Signale neu laden, falls im Signal implementiert
        self.FsigA.update()
        self.FsigB.update()
        # Je nach Signaltyp Funktion durchführen
        if self.FsigA.FTyp == self.FsigB.FTyp:
            if self.FTyp ==  self.RS_Typ_discrete:
                if (self.FsigA.getYAt(ATime)  != None) and (self.FsigB.getYAt(ATime) != None) :
                        return np.add(self.FsigA.getYAt(ATime),self.FsigB.getYAt(ATime))
                return None
            elif self.FTyp == self.RS_Typ_continuous:
                return  self.FsigA.getYAt(ATime) + self.FsigB.getYAt(ATime)
            elif self.FTyp == self.RS_Typ_complex:
                return  None
            else:
                return  None
        else:
            print(self.RS_ERROR_1)                 
        return None # Default Ausgabe wenn kein If erfüllt wird   
# ----------------------------------------------- ENDE DEF -----------------------------------------------      
    # Konvertiert Komplexes-Eingabeformat zu Komplexem-Numpy-Format (True) oder behält Komplexes-Eingabeformat bei   
    def getZ(self,AAsNumpy=False):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
                if not AAsNumpy:
                    return self.FsigA.getZ() + self.FsigB.getZ()
                else:
                    return np.array(self.FsigA.getZ() + self.FsigB.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird    
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Realteil der komplexen Zahl zurück        
    def getRe(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
             return self.FsigA.getRe() + self.FsigB.getRe()

        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird          
# ----------------------------------------------- ENDE DEF -----------------------------------------------   
    # Gibt den Imaginärteil der komplexen Zahl zurück     
    def getIm(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
              return self.FsigA.getIm() + self.FsigB.getIm()          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
# ----------------------------------------------- ENDE DEF -----------------------------------------------    
    # Gibt den Polaren-Winkel der komplexen Zahl zurück(Grad, oder Rad)   
    def getAngle(self,ADegree = True):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird        
# ----------------------------------------------- ENDE DEF -----------------------------------------------     
    # Gibt den Betrag der komplexen Zahl zurück    
    def getAbs(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
# ----------------------------------------------- ENDE DEF -----------------------------------------------      
    # Plotten neu definieren um die Liste der Zeiger zuübergeben bei komplexen Zahlen 
    def plot(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FsigA.getZ()],[self.FsigA.getZ(),self.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,[self.RS_Signal_A,self.RS_Signal_B, self.RS_Signal_AB])
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird      
# ----------------------------------------------- ENDE DEF -----------------------------------------------  
    # ggf. Sigale Updaten, fall implementiert    
    def update(self):         
        self.FsigA.update()
        self.FsigB.update()
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl 
    def __str__(self):
        return self.FsigA.__str__() + "+" + self.FsigB.__str__()
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


# Subtarieren zweier Signale gleichen Types
class sub(signal):
    def __init__(self, ASignalA, ASignalB):
    # Initialisierung der Basisklasse
        super().__init__(ASignalA.FTyp )
    # =============================================== verwendete Texte ===============================================
        self.RS_Signal_A = 'Signal A'
        self.RS_Signal_B = 'Signal B'
        self.RS_Signal_AB = 'Signal A-B'
    # =============================================== def übergreifende Variablen ===============================================           
        self.FSigA = ASignalA
        self.FSigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal A neu
    def setSigA(self, ASignalA):
        self.FSigA = ASignalA
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal B neu
    def setSigB(self, ASignalB):
        self.FSigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, ATime):
        return self.FSigA.getYAt(ATime) - self.FSigB.getYAt(ATime)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Konvertiert Komplexes-Eingabeformat zu Komplexem-Numpy-Format (True) oder behält Komplexes-Eingabeformat bei          
    def getZ(self,AAsNumpy=False):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
                if not AAsNumpy:
                    return self.FSigA.getZ() - self.FSigB.getZ()
                else:
                    return np.array(self.FSigA.getZ() - self.FSigB.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird    
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Realteil der komplexen Zahl zurück        
    def getRe(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
             return self.FSigA.getRe() - self.FSigB.getRe()

        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird   
# ----------------------------------------------- ENDE DEF -----------------------------------------------        
    # Gibt den Imaginärteil der komplexen Zahl zurück        
    def getIm(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
              return self.FSigA.getIm() - self.FSigB.getIm()          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Polaren-Winkel der komplexen Zahl zurück(Grad, oder Rad)      
    def getAngle(self,ADegree = True):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird     
# ----------------------------------------------- ENDE DEF -----------------------------------------------    
    # Gibt den Betrag der komplexen Zahl zurück        
    def getAbs(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Plotten neu definieren um die Liste der Zeiger zuübergeben bei komplexen Zahlen      
    def plot(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FSigA.getZ()],[self.FSigA.getZ(),self.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,[self.RS_Signal_A,self.RS_Signal_B, self.RS_Signal_AB])
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              

# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl 
    def __str__(self):
        return self.sigA.__str__() + "-" + self.sigB.__str__()
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  



# Multiplizieren zweier Signale gleichen Types
class mul(signal):
    def __init__(self, ASignalA, ASignalB):
    # Initialisierung der Basisklasse
        super().__init__(ASignalA.FTyp )
    # =============================================== verwendete Texte ===============================================
        self.RS_Signal_A = 'Signal A'
        self.RS_Signal_B = 'Signal B'
        self.RS_Signal_AB = 'Signal A*B'
    # =============================================== def übergreifende Variablen ===============================================  
        self.FsigA = ASignalA
        self.FsigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal A neu
    def setSigA(self, ASignalA):
        self.FsigA = ASignalA
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal B neu
    def setSigB(self, ASignalB):
        self.FsigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, ATime):
        return self.FsigA.getYAt(ATime) * self.FsigB.getYAt(ATime)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Konvertiert Komplexes-Eingabeformat zu Komplexem-Numpy-Format (True) oder behält Komplexes-Eingabeformat bei          
    def getZ(self,AAsNumpy=False):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
                if not AAsNumpy:
                    return self.FsigA.getZ() * self.FsigB.getZ()
                else:
                    return np.array(self.FsigA.getZ() * self.FsigB.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird    
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Realteil der komplexen Zahl zurück        
    def getRe(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return self.getZ().real
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird       
# ----------------------------------------------- ENDE DEF -----------------------------------------------    
    # Gibt den Imaginärteil der komplexen Zahl zurück       
    def getIm(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
             return self.getZ().imag          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
       
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Polaren-Winkel der komplexen Zahl zurück(Grad, oder Rad)  
    def getAngle(self,ADegree = True):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird        
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Betrag der komplexen Zahl zurück        
    def getAbs(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Plotten neu definieren um die Liste der Zeiger zuübergeben bei komplexen Zahlen      
    def plot(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FsigA.getZ()],[0,self.FsigB.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,[self.RS_Signal_A,self.RS_Signal_B, self.RS_Signal_AB])
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird  
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl 
    def __str__(self):
        return self.sigA.__str__() + "*" + self.sigB.__str__()
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  


# Dividieren zweier Signale gleichen Types
class div(signal):
    def __init__(self, ASignalA, ASignalB):
    # Initialisierung der Basisklasse
        super().__init__(ASignalA.FTyp )
    # =============================================== verwendete Texte ===============================================
        self.RS_Signal_A = 'Signal A'
        self.RS_Signal_B = 'Signal B'
        self.RS_Signal_AB = 'Signal A/B'
    # =============================================== def übergreifende Variablen ===============================================  
        self.FsigA = ASignalA
        self.FsigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal A neu
    def setSigA(self, ASignalA):
        self.FsigA = ASignalA
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal B neu
    def setSigB(self, ASignalB):
        self.FsigB = ASignalB
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, ATime):
        return self.FsigA.getYAt(ATime) / self.FsigB.getYAt(ATime)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Konvertiert Komplexes-Eingabeformat zu Komplexem-Numpy-Format (True) oder behält Komplexes-Eingabeformat bei          
    def getZ(self,AAsNumpy=False):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
                if not AAsNumpy:
                    return self.FsigA.getZ() / self.FsigB.getZ()
                else:
                    return np.array(self.FsigA.getZ() / self.FsigB.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird    
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Realteil der komplexen Zahl zurück        
    def getRe(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return self.getZ().real

        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird          
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Imaginärteil der komplexen Zahl zurück        
    def getIm(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return self.getZ().imag          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den Polaren-Winkel der komplexen Zahl zurück(Grad, oder Rad)     
    def getAngle(self,ADegree = True):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird      
# ----------------------------------------------- ENDE DEF -----------------------------------------------   
    # Gibt den Betrag der komplexen Zahl zurück        
    def getAbs(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird         
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Plotten neu definieren um die Liste der Zeiger zuübergeben bei komplexen Zahlen       
    def plot(self):
        # Je nach Signaltyp Funktion durchführen
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FsigA.getZ()],[0,self.FsigB.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,[self.RS_Signal_A,self.RS_Signal_B, self.RS_Signal_AB]) 
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird  
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Ausgabe der Eingabe beim Printbefehl 
    def __str__(self):
        return self.sigA.__str__() + "/" + self.sigB.__str__()
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  

# Verschiebung
class shift(signal):
    def __init__(self, ASignal, AOffset):

    # Initialisierung der Basisklasse
        super().__init__(ASignal.FTyp)
    # =============================================== def übergreifende Variablen ===============================================  
        super().__init__(ASignal.FTyp)
        self.FSignal = ASignal
        self.FOffset = AOffset
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Signal neu
    def setSignal(self, ASignal):
        self.FSignal = ASignal
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Setzt das Offset neu
    def setOffset(self, AOffset):
        self.FOffset = AOffset
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, time):
        return self.FSignal.getYAt(time + self.FOffset)
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  

# Faltung
class convolve(discrete):
    def __init__(self, ASignalA, ASignalB, ASamplRate = 1, AStart = 0, AEnd = 100):
    # Initialisierung der Basisklasse
        super().__init__("discrete")
    # =============================================== def übergreifende Variablen ===============================================  
        self.FSigA = ASignalA
        self.FSigB = ASignalB
        self.FSamplingRate = ASamplRate
        self.FStart = AStart
        self.FEnd = AEnd
        self.FList = []
        self.FConv = None
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Gibt den y-Wert für einen gegebenen x-Wert zurück 
    def getYAt(self, ATime):
        try:
            self.update()
            xList = self.FSigA.getXList()
            i = xList.index(ATime)
            yList = self.FConv.tolist()
            out = yList[i]
        except ValueError:
            out = None
        return out
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Setzt die SmapleRate neu 
    def setSamplRate(self, ASamplRate):
        self.FSamplingRate = ASamplRate
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Berechnet die Faltung neu
    def update(self):
        self.FList = np.arange(self.FStart, self.FEnd, self.FSamplingRate)
        AVals = self.FSigA.getList(self.FList)
        BVals = self.FSigB.getList(self.FList)
        print('AVals'  + str(AVals))
        print('BVals'  + str(AVals))
        self.FConv = np.convolve(AVals, BVals)
# ----------------------------------------------- ENDE DEF -----------------------------------------------
    # Y-Werte an X Stellen berechnen -> Liste erzeugen
    def getList(self, AInList):
        AVals = self.FSigA.getList(AInList)
        BVals = self.FSigB.getList(AInList)
        outList = np.convolve(AVals, BVals).tolist()
        del outList[len(AVals):] 
        return outList
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  




# Mögliche Erweiterung: Import von Dateien. Beispiel Signal.csv im Ansatz gegeben:     
# nocht nicht 100 % auf Funktion geprüft   
class List(discrete):
    def __init__(self, AFilePath):
    # Initialisierung der Basisklasse
        super().__init__("discrete")
    # =============================================== def übergreifende Variablen ===============================================  
#        self.FFilePath = 'sinus.csv'
        self.FFilePath = AFilePath
        self.FxList = None
        self.FyList = None
    # =============================================== nach init auszuführende def  ===============================================
        # Datei aus Lesen und Werte speichern
        self.read()
 # ----------------------------------------------- ENDE DEF -----------------------------------------------       
    def read(self):        
        ffile  = open(self.FFilePath)
        read = csv.reader(ffile)
        self.FxList = []
        self.FyList = []
        for row in read :
            self.FxList = self.FxList + [float(row[0])]
            self.FyList = self.FyList + [float(row[1])]
# ----------------------------------------------- ENDE DEF -----------------------------------------------     
    def getYAt(self, Time):

        try:            
            i =  self.FxList.index(Time)
            out = self.FyList[i]
        except ValueError:
            out = None
        return out  
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
    def getList(self, InList = None):
        outList = [False,[self.FxList],[self.FyList]]
        return outList
# ----------------------------------------------- ENDE DEF ----------------------------------------------- 
# +++++++++++++++++++++++++++++++++++++++++++++++ ENDE CLASS +++++++++++++++++++++++++++++++++++++++++++++  