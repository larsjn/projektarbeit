from abc import ABCMeta, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import lib.Input_Function as fct



# Signal-Basisklasse - muss von allen Signal-Klassen implementiert werden
class signal(metaclass=ABCMeta):
    @abstractmethod

    def getYAt(self, x):
        pass

    def getList(self, inList):
        outList = [self.getYAt(x) for x in inList]
        return outList
    
class create(signal):
    def __init__ (self):
        self.FFunction = None    
        self.FFunction = fct.Class_Create_New_Function()
        h=self.FFunction.Create(None)
        
    def delete_Values(self):
        if self.FFunction != None:
            del self.FFunction
            self.FFunction = None
    def getXnparray(self):
        if self.FFunction != None:
            return self.FFunction.FxWerte
        
    def getYnparray(self):
        if self.FFunction != None:
            return self.FFunction.FyWerte   
            
    def getXList(self):
        if self.FFunction != None:
            return self.FFunction.FxWerte.tolist()
        
    def getYList(self):
        if self.FFunction != None:
            return self.FFunction.FyWerte.tolist()   

    def getYAt(self,Ax):
        try:
            xList = self.FFunction.FxWerte.tolist()
            i = xList.index(Ax)
            yList = self.FFunction.FyWerte.tolist()
            out = yList[i]
        except ValueError:
            out = None
        return out
            
    def getList(self, inList):
        outList = [self.getYAt(x) for x in inList]
        return outList
        
        
        
# Kontinuierliche Signale
class sine(signal):
    def __init__(self, frequency = 1, amplitude = 1):
        self.frequency = frequency
        self.amplitude = amplitude

    def getYAt(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time)

    def setFreq(self, frequency):
        self.frequency = frequency

    def setAmp(self, amplitude):
        self.amplitude = amplitude

    def update(self):
        self.frequency = self.sfreq.val
        self.amplitude = self.samp.val


class cosine(signal):
    def __init__(self, frequency = 1, amplitude = 1):
        self.frequency = frequency
        self.amplitude = amplitude

    def getYAt(self, time):
        return self.amplitude * np.cos(2 * np.pi * self.frequency * time)

    def setFreq(self, frequency):
        self.frequency = frequency

    def setAmp(self, amplitude):
        self.amplitude = amplitude


class square(signal):
    def __init__(self, frequency = 1, amplitude = 1, dutyCycle = 0.5):
        self.frequency = frequency
        self.amplitude = amplitude
        self.dutyCycle = dutyCycle
        self.update()

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


class const(signal):
    def __init__(self, value):
        self._value = value

    def getYAt(self, x):
        return self._value

    def setValue(self, value):
        self._value = value


# Rechenoperationen
class add(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def setSigA(self, signalA):
        self.sigA = signalA

    def setSigB(self, signalB):
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) + self.sigB.getYAt(time)


class sub(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def setSigA(self, signalA):
        self.sigA = signalA

    def setSigB(self, signalB):
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) - self.sigB.getYAt(time)


class mul(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def setSigA(self, signalA):
        self.sigA = signalA

    def setSigB(self, signalB):
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) * self.sigB.getYAt(time)


class div(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def setSigA(self, signalA):
        self.sigA = signalA

    def setSigB(self, signalB):
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) / self.sigB.getYAt(time)

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
class convolve(signal):
    def __init__(self, signalA, signalB, samplRate = 1, start = 0, end = 100):
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
#        
#        return self.conv[time]

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
