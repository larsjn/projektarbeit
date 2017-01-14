from abc import ABCMeta, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import lib.create_function_widgets as fct
import lib.create_komplex as kpl
import operator as op
import lib.Plot_Widget as sigplt
import parser
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
        
        self.FSignal = None
         
    
    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return sub(self, other)

    def __mul__(self, other):
        return mul(self, other)

    def __truediv__(self, other):
        return div(self, other)
        
    def getYAt(selfe,Ax):
         pass
        
    def getXList(self):        
        return None 
 #   def getYList(self):        
 #       return None 
        
    def getList(self, inList):
  
        if (self.FTyp == self.RS_Typ_discrete) or (self.FTyp == self.RS_Typ_continuous) :
            outList = [self.getYAt(x) for x in inList]
            return outList
        elif self.FTyp == self.RS_Typ_complex:
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird  
   
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
        
    def plot(self, samplingRate = 1, start = 0, end = 100):
        if self.FTyp ==  self.RS_Typ_discrete:
            sigplt.Class_Plot_Menu(self)                    
            return  None
        elif self.FTyp == self.RS_Typ_continuous:
            return  None
        elif self.FTyp == self.RS_Typ_complex:
            sigplt.Class_Plot_Menu(self)
            return  None
        else:
            return  None              
        return None # Default Ausgabe wenn kein If erfüllt wird  

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

    def getYAt(self, time):
        t = time
return eval(self.function)

# Eine Signal per Bildungsvorschrift erzeugen
class create(signal):
    def __init__ (self, Atype): 


        super().__init__(Atype)  

                 
        if Atype == self.RS_Typ_discrete :
            self.FComplex = None
            self.FisDiscrete = True
            self.FFunction = fct.Class_Create_New_Function(self.FisDiscrete)
            self.FFunction.Create(None)
            
        elif Atype ==  self.RS_Typ_continuous:
            self.FComplex = None
            self.FisDiscrete = False
            self.FFunction = fct.Class_Create_New_Function(self.FisDiscrete)
            self.FFunction.Create(None)
            
        elif Atype ==  self.RS_Typ_complex:
            self.FFunction = None
            self.FComplex = kpl.create_complex()               
        else:
            print("Mögliche Parameter:"+ self.RS_Typ_discrete+","+self.RS_Typ_continuous+","+self.RS_Typ_complex)            

   
        self.FxList = None
        self.FyList = None
  
            
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
        if self.FTyp ==  self.RS_Typ_discrete:
            if self.FFunction != None:
                try:
                    self.update()
                    xList = self.FxList
                    i = xList.index(Ax)
                    yList = self.FyList
                    out = yList[i]
                except ValueError:
                    out = None
                return out        
        elif self.FTyp == self.RS_Typ_continuous:

            return self.FFunction.FResultSignal.getYAt(Ax)
        elif self.FTyp == self.RS_Typ_complex:
            return None
        else:
            return None               
        return None # Default Ausgabe wenn kein If erfüllt wird      
    def __str__(self):
        if self.FTyp == self.RS_Typ_discrete:
            return self.FFunction.FResultSignal.__str__()
        else:
            print("Signal ist nicht kontinuierlich")
        return None # Default Ausgabe wenn kein If erfüllt wird  
        

    def update(self):
        if self.FTyp ==  self.RS_Typ_discrete:
            if self.FFunction != None:           
                if isinstance(self.FFunction.FxWerte, (list)): # Prüfen ob schon eine Liste
                       self.FxList = self.FFunction.FxWerte
                else:
                       self.FxList = self.FFunction.FxWerte.tolist()    
                                 
                if isinstance(self.FFunction.FyWerte, (list)): # Prüfen ob schon eine Liste
                       self.FyList = self.FFunction.FyWerte
                else:
                       self.FyList = self.FFunction.FxWerte.tolist()   
        elif self.FTyp == self.RS_Typ_continuous:
            return None
        elif self.FTyp == self.RS_Typ_complex:
            return None
        else:
            return None                     
        return None # Default Ausgabe wenn kein If erfüllt wir
        
        
    def getXList(self):  
        if self.FFunction != None: 
            self.update()
            return self.FxList  
 #   def getYList(self):
 #       if self.FFunction != None: 
 #           self.update()
  #          return self.FyList
        
        
# Kontinuierliche Signale
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
        self.frequency = self.sfreq.val
        self.amplitude = self.samp.val

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

# ToDo: Dreieck, Sägezahn


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


# Rechenoperationen
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
                if (self.FsigA.getYAt(Atime)  != None) and (self.FsigB.getYAt(Atime)!= None) :                     
                        return np.add(self.FsigA.getYAt(Atime),self.FsigB.getYAt(Atime)).tolist()
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
        
    def getXList(self):
        if self.FsigA.FTyp == self.FsigB.FTyp:
            if self.FTyp ==  self.RS_Typ_discrete: 
                xA = self.FsigA.getXList()
                xB = self.FsigB.getXList()
                
                if xA == xB and xA != None:
                    return xA
                else: 
                    print('ERROR: X-Listen unterscheiden sich')
        return  None   
    def update(self):         
        self.FsigA.update()
        self.FsigB.update()         
       
    def __str__(self):
        return self.FsigA.__str__() + "+" + self.FsigB.__str__()


class sub(signal):
    def __init__(self, signalA, signalB):
        super().__init__(AsignalA.FTyp ) 
        self.sigA = signalA
        self.sigB = signalB

    def setSigA(self, signalA):
        self.sigA = signalA

    def setSigB(self, signalB):
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) - self.sigB.getYAt(time)

    def __str__(self):
        return self.sigA.__str__() + "-" + self.sigB.__str__()


class mul(signal):
    def __init__(self, signalA, signalB):
        super().__init__(AsignalA.FTyp ) 
        self.sigA = signalA
        self.sigB = signalB

    def setSigA(self, signalA):
        self.sigA = signalA

    def setSigB(self, signalB):
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) * self.sigB.getYAt(time)

    def __str__(self):
        return self.sigA.__str__() + "*" + self.sigB.__str__()


class div(signal):
    def __init__(self, signalA, signalB):
        super().__init__(AsignalA.FTyp ) 
        self.sigA = signalA
        self.sigB = signalB

    def setSigA(self, signalA):
        self.sigA = signalA

    def setSigB(self, signalB):
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) / self.sigB.getYAt(time)

    def __str__(self):
        return self.sigA.__str__() + "/" + self.sigB.__str__()

# Verschiebung
class shift(signal):
    def __init__(self, signal, offset):
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
        self.sigA = signalA
        self.sigB = signalB
        self.samplingRate = samplRate
        self.start = start
        self.end = end
        self.type = "discrete"

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
        return np.convolve(AVals, BVals)

# ToDo: Stauchung
