import lib.createcomplexsignal as kpl
import lib.createsignal as inp
import lib.plotwidget as sigplt
import numpy as np
import parser
import csv
from abc import ABCMeta, abstractmethod
from math import *

# Signal-Basisklasse - muss von allen Signal-Klassen implementiert werden
class signal(metaclass=ABCMeta):

    def __init__ (self, Atype = None):
        self.RS_Typ_discrete    = "discrete"
        self.RS_Typ_continuous = "continuous"
        self.RS_Typ_complex     = "complex"
        self.RS_ERROR_Listenlaenge = 'ERROR: Länge der X und Y Listen unterscheiden sich. X-Liste zuerst setzten'
        self.FTyp = Atype
        self.FComplex = None
        self.FComplex
        self.FSignal = None

#Operatorüberladungen für Rechenoperationen
    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return sub(self, other)

    def __mul__(self, other):
        return mul(self, other)

    def __truediv__(self, other):
        return div(self, other)

#Y-Wert an stelle X berechnen        
    def getYAt(selfe,Ax):
         pass
     
#X-Werte-Liste eines diskreten Signals falls vorhanden
    def getXList(self):
        return None
        
#Y-Werte an X Stellen berechnen -> Liste erzeugen
    def getList(self, inList):

        if (self.FTyp == self.RS_Typ_discrete) or (self.FTyp == self.RS_Typ_continuous) :
            outList = [self.getYAt(x) for x in inList]
            return outList
        elif self.FTyp == self.RS_Typ_complex:
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird

#Konvertiert Komplexes-Eingabeformat zu Komplexem-Numpy-Format (True) oder behält Komplexes-Eingabeformat bei      
    def getZ(self,AAsNumpy=False):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:
                if not AAsNumpy:
                    return self.FComplex.FZ
                else:
                    return np.array(self.FComplex.FZ)
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird

#Gibt den Realteil der komplexen Zahl zurück
    def getRe(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:
               return self.FComplex.FRe
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird
        
#Gibt den Imaginärteil der komplexen Zahl zurück
    def getIm(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:
               return self.FComplex.FIm
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird

#Gibt den Polaren-Winkel der komplexen Zahl zurück(Grad, oder Rad)
    def getAngle(self,ADegree = True):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:
                if ADegree:
                    return self.FComplex.FAngle
                else:
                    return self.FComplex.FAngleRad
            return  None
        else:
            return  None
        return None # Default Ausgabe wenn kein If erfüllt wird

#Gibt den Betrag der komplexen Zahl zurück
    def getAbs(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            if self.FComplex  != None:
                    return self.FComplex.FAbsolute
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              

#Plottet Signale      
    def plot(self):
        sigplt.Class_Plot_Menu(self)
        return None 
        
#Updated Klassenvariablen 
    def update(self):
        pass


# Basis-Klasse für kontinuierliche Signale
class contiuous(signal):
    # Gibt den y-Wert für einen gegebenen x-Wert zurück
    @abstractmethod
    def getYAt(self, x):
        pass

# Basis-Klasse für diskrete Signale
class discrete(signal):
    pass

# Basis-Klasse für Rechenoperationen (?)

# Nutzereingabe Parsen
class parseFkt(signal):
    def __init__(self, formula):
        self.function = parser.expr(formula).compile()

        super().__init__(None)
        self.FTyp = self.RS_Typ_continuous

    def getYAt(self, time):
        t = time                    #Selbst wenn Spyder oder ein anderer Kompiler hier meckert. Das muss so!!!!
        return eval(self.function)

# Eine Signal per Bildungsvorschrift erzeugen
class create(signal):
    def __init__ (self, Atype):
        #Initialisierung der Basisklasse
        super().__init__(Atype)
        #Funktion als String (Parsereingabe zwischenspeicher)
        self.input = None
        #Erzeugen der Eingbaemaske je nach gewähltem Typ
        if Atype == self.RS_Typ_continuous:
            self.FComplex = None
            self.FFunction = inp.Class_Input_Parser(True)
        elif Atype == self.RS_Typ_discrete:
            self.FComplex = None
            self.FFunction = inp.Class_Input_Parser(False)
        elif Atype == self.RS_Typ_complex:
            self.FFunction = None
            self.FComplex = kpl.create_complex()
        else:
            print("Mögliche Parameter:"+ self.RS_Typ_discrete+","+self.RS_Typ_continuous+","+self.RS_Typ_complex)

        #self.FxList = None         LEGACY UNFUG
        #self.FyList = None

#Vorsorgliche Speicherfreigabe implementierung (unused)
    def delete_Values(self):
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
     
    def getYAt(self,Ax): 
        if (self.FTyp ==  self.RS_Typ_discrete ) or (self.FTyp == self.RS_Typ_continuous):
            #Wenn sich die Eingabefunktion geändert hat: Neu parsen. Sonst bestehende Funktion verwenden
            if self.FFunction.FInput != self.input:
                self.parsedFktn = parseFkt(self.FFunction.FInput)
                self.input = self.FFunction.FInput
                return self.parsedFktn.getYAt(Ax)
            else:
                return self.parsedFktn.getYAt(Ax)
        elif self.FTyp == self.RS_Typ_complex:
            return None
        else:
            return None
        return None # Default Ausgabe wenn kein If erfüllt wird

#Ausgabe der Eingabe beim Printbefehl        
    def __str__(self):
        if (self.FTyp ==  self.RS_Typ_discrete ) or (self.FTyp == self.RS_Typ_continuous):
            return self.input
        else:
            print("Signal ist nicht kontinuierlich oder diskret")

        return None # Default Ausgabe wenn kein If erfüllt wird  

   # def getXList(self):
   #    if self.FFunction != None:
   #       self.update()
   #       return self.FxList


# Kontinuierliche Signale - Klassendefinitonen 
class sine(contiuous):
    def __init__(self, frequency = 1, amplitude = 1):
        self.frequency = float(frequency)
        self.amplitude = float(amplitude)
        super().__init__("continuous")

    def getYAt(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time)

    def setFreq(self, frequency):
        self.frequency = frequency

    def setAmp(self, amplitude):
        self.amplitude = amplitude

    def update(self):
        self.frequency = self.frequency
        self.amplitude = self.amplitude

    def __str__(self):
        return "{0}*sin(2*PI*{1}*t)".format(self.amplitude, self.frequency)

class cosine(contiuous):
    def __init__(self, frequency = 1, amplitude = 1):
        self.frequency = float(frequency)
        self.amplitude = float(amplitude)
        super().__init__("continuous")

    def getYAt(self, time):
        return self.amplitude * np.cos(2.0 * np.pi * self.frequency * time)

    def setFreq(self, frequency):
        self.frequency = frequency

    def setAmp(self, amplitude):
        self.amplitude = amplitude

    def __str__(self):
        return "{0}*cos(2*PI*{1}*t)".format(self.amplitude, self.frequency)


class square(contiuous):
    def __init__(self, frequency = 1, amplitude = 1, dutyCycle = 0.5):
        self.frequency = frequency
        self.amplitude = amplitude
        self.dutyCycle = dutyCycle
        self.update()
        super().__init__("continuous")

    def getYAt(self, time):
        if((time % self.time) < self.onTime):
            return self.amplitude
        else: return - self.amplitude

    def setFreq(self, frequency):
        self.frequency = frequency
        self.update()

    def setAmp(self, amplitude):
        self.amplitude = amplitude

    def setDutyCycle(self, dutyCycle):
        self.dutyCycle = dutyCycle

    def update(self):
        self.time = 1 / self.frequency
        self.onTime = self.time * self.dutyCycle

#Erweiterungsmöglichkeiten, z.B.: Dreieck oder Sägezahn Funktionsklassen


class const(contiuous):
    def __init__(self, value):
        self.value = value
        super().__init__("continuous")

    def getYAt(self, x):
        return self.value

    def setValue(self, value):
        self._value = value

    def __str__(self):
        return str(self.value)

class contToDisc(signal):
    def __init__(self, signal, samplingRate=100, start=0, end=10):
        self.xList = np.arange(start, end, 1 / samplingRate)
        self.yList = signal.getList(self.xList)

    def getXList(self):
        return self.xList

    def getYList(self):
        return self.yList


# Rechenoperationen Klassendefinitionen
class add(signal):
    def __init__(self, AsignalA, AsignalB):

        super().__init__(AsignalA.FTyp )

        self.FsigA = AsignalA
        self.FsigB = AsignalB

    def setSigA(self, AsignalA):
        self.FsigA = AsignalA

    def setSigB(self, AsignalB):
        self.FsigB = AsignalB

    def getYAt(self, Atime):
        self.FsigA.update()
        self.FsigB.update()

        if self.FsigA.FTyp == self.FsigB.FTyp:
            if self.FTyp ==  self.RS_Typ_discrete:
                if (self.FsigA.getYAt(Atime)  != None) and (self.FsigB.getYAt(Atime) != None) :
                        return np.add(self.FsigA.getYAt(Atime),self.FsigB.getYAt(Atime))
                return None
            elif self.FTyp == self.RS_Typ_continuous:
                return  self.FsigA.getYAt(Atime) + self.FsigB.getYAt(Atime)
            elif self.FTyp == self.RS_Typ_complex:
                return  None
            else:
                return  None
        else:
            print('ERROR: Signaltypen unterscheiden sich')                 
        return None # Default Ausgabe wenn kein If erfüllt wird   
        
    def getZ(self,AAsNumpy=False):
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
        
    def getRe(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
             return self.FsigA.getRe() + self.FsigB.getRe()

        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird          
        
    def getIm(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
              return self.FsigA.getIm() + self.FsigB.getIm()          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def getAngle(self,ADegree = True):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird        
        
    def getAbs(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def plot(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
                 # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FsigA.getZ()],[self.FsigA.getZ(),self.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,['Signal A','Signal B', 'Signal A+B'])
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird      
        
        
        
        
    def update(self):         
        self.FsigA.update()
        self.FsigB.update()

    def __str__(self):
        return self.FsigA.__str__() + "+" + self.FsigB.__str__()


class sub(signal):
    def __init__(self, AsignalA, AsignalB):
        super().__init__(AsignalA.FTyp ) 
        self.FsigA = AsignalA
        self.FsigB = AsignalB

    def setSigA(self, AsignalA):
        self.FsigA = AsignalA

    def setSigB(self, AsignalB):
        self.FsigB = AsignalB

    def getYAt(self, Atime):
        return self.FsigA.getYAt(Atime) - self.FsigB.getYAt(Atime)
        
    def getZ(self,AAsNumpy=False):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
                if not AAsNumpy:
                    return self.FsigA.getZ() - self.FsigB.getZ()
                else:
                    return np.array(self.FsigA.getZ() - self.FsigB.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird    
        
    def getRe(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
             return self.FsigA.getRe() - self.FsigB.getRe()

        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird          
        
    def getIm(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
              return self.FsigA.getIm() - self.FsigB.getIm()          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def getAngle(self,ADegree = True):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird        
        
    def getAbs(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def plot(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
                 # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FsigA.getZ()],[self.FsigA.getZ(),self.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,['Signal A','Signal B', 'Signal A-B'])
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              


    def __str__(self):
        return self.sigA.__str__() + "-" + self.sigB.__str__()


class mul(signal):
    def __init__(self, AsignalA, AsignalB):
        super().__init__(AsignalA.FTyp ) 
        self.FsigA = AsignalA
        self.FsigB = AsignalB

    def setSigA(self, AsignalA):
        self.FsigA = AsignalA

    def setSigB(self, AsignalB):
        self.FsigB = AsignalB

    def getYAt(self, Atime):
        return self.FsigA.getYAt(Atime) * self.FsigB.getYAt(Atime)
        
    def getZ(self,AAsNumpy=False):
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
        
    def getRe(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return self.getZ().real
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird          
        
    def getIm(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
             return self.getZ().imag          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def getAngle(self,ADegree = True):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird        
        
    def getAbs(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def plot(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
                 # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FsigA.getZ()],[0,self.FsigB.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,['Signal A','Signal B', 'Signal A*B'])
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird  

    def __str__(self):
        return self.sigA.__str__() + "*" + self.sigB.__str__()


class div(signal):
    def __init__(self, AsignalA, AsignalB):
        super().__init__(AsignalA.FTyp ) 
        self.FsigA = AsignalA
        self.FsigB = AsignalB

    def setSigA(self, AsignalA):
        self.FsigA = AsignalA

    def setSigB(self, AsignalB):
        self.FsigB = AsignalB

    def getYAt(self, Atime):
        return self.FsigA.getYAt(Atime) / self.FsigB.getYAt(Atime)
        
    def getZ(self,AAsNumpy=False):
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
        
    def getRe(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return self.getZ().real

        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird          
        
    def getIm(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return self.getZ().imag          
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def getAngle(self,ADegree = True):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:              
            return np.angle(self.getZ(),ADegree)       
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird        
        
    def getAbs(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None           
        elif self.FTyp == self.RS_Typ_complex:
            return np.absolute(self.getZ())
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird              
      
    def plot(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            sigplt.Class_Plot_Menu(self)  
            return  None
        elif self.FTyp == self.RS_Typ_complex:
                 # Layout der Liste [[ZInAStart,ZInAEnd],[ZInBStart,ZInBStart],[ZOutStart,ZOutEnd]]   
            ToPlot = [[0,self.FsigA.getZ()],[0,self.FsigB.getZ()],[0,self.getZ()]]            
            sigplt.Class_Plot_Menu(self,ToPlot,['Signal A','Signal B', 'Signal A/B'])
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird  

    def __str__(self):
        return self.sigA.__str__() + "/" + self.sigB.__str__()

# Verschiebung
class shift(signal):
    def __init__(self, signal, offset):
        super().__init__(signal.FTyp)
        self.signal = signal
        self.offset = offset

    def setSignal(self, signal):
        self.signal = signal

    def setOffset(self, offset):
        self.offset = offset

    def getYAt(self, time):
        return self.signal.getYAt(time + self.offset)

# Faltung
class convolve(discrete):
    def __init__(self, signalA, signalB, samplRate = 1, start = 0, end = 100):
        super().__init__("discrete")
        self.sigA = signalA
        self.sigB = signalB
        self.samplingRate = samplRate
        self.start = start
        self.end = end

    def getYAt(self, time):

        try:
            self.update()
            xList = self.sigA.getXList()
            i = xList.index(time)
            yList = self.conv.tolist()
            out = yList[i]
        except ValueError:
            out = None
        return out

    def setSamplRate(self, samplRate):
        self.samplingRate = samplRate

    def update(self):

        self.list = np.arange(self.start, self.end, self.samplingRate)
        AVals = self.sigA.getList(self.list)
        BVals = self.sigB.getList(self.list)
        print('AVals'  + str(AVals))
        print('BVals'  + str(AVals))

        self.conv = np.convolve(AVals, BVals)

    def getList(self, inList):
        AVals = self.sigA.getList(inList)
        BVals = self.sigB.getList(inList)
        outList = np.convolve(AVals, BVals).tolist()
        del outList[len(AVals):] 
        return outList

# Mögliche Erweiterung: Import von Dateien. Beispiel Signal.csv im Ansatz gegeben:        
class List(discrete):
    def __init__(self, AFilePath):
        super().__init__("discrete")
        self.FFilePath = AFilePath
        self.xList = None
        self.yList = None
        self.read()
       
    def read(self):        
        ffile  = open(self.FFilePath)
        read = csv.reader(ffile)
        self.xList = []
        self.yList = []
        for row in read :
            self.xList = self.xList + [float(row[0])]
            self.yList = self.yList + [float(row[1])]
    
    def getYAt(self, time):

        try:            
            i =  self.xList.index(time)
            out = self.yList[i]
        except ValueError:
            out = None
        return out  

    def getList(self, inList):
        outList = [False,[self.xList],[self.yList]]
        return outList
