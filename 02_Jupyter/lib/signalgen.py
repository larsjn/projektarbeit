from abc import ABCMeta, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import lib.create_function_widgets as fct
import operator as op
import parser
from math import *

# Signal-Basisklasse - muss von allen Signal-Klassen implementiert werden
class signal(metaclass=ABCMeta):
    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return sub(self, other)

    def __mul__(self, other):
        return mul(self, other)

    def __truediv__(self, other):
        return div(self, other)

    def getList(self, inList):

        outList = [self.getYAt(x) for x in inList]
        return outList

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
    def __init__ (self, type):
        if type == "discrete":
            self.isDiscrete = True
        elif type == "continuous":
            self.isDiscrete = False
        else:
            print("Mögliche Parameter: discrete, continuous")
            return None

        self.function = fct.Class_Create_New_Function(self.isDiscrete)
        self.function.Create(None)

    def delete_Values(self):
        if self.function != None:
            del self.function
            self.function = None

    def getXnparray(self):
        if self.function != None:
            return self.function.FxWerte

    def getYnparray(self):
        if self.function != None:
            return self.function.FyWerte

    def getXList(self):
        if self.function != None:
            return self.function.FxWerte.tolist()

    def getYList(self):
        if self.function != None:
            return self.function.FyWerte.tolist()

    def getYAt(self, time):
        if self.isDiscrete == False:
            return self.function.FResultSignal.getYAt(time)

        else:
            print("Signal ist nicht kontinuierlich")
            return None
        # try:
        #     xList = self.function.FxWerte.tolist()
        #     i = xList.index(Ax)
        #     yList = self.function.FyWerte.tolist()
        #     out = yList[i]
        # except ValueError:
        #     out = None
        # return out

    def getList(self, inList):
        outList = [self.getYAt(x) for x in inList]
        return outList

    def __str__(self):
        if self.isDiscrete == False:
            return self.function.FResultSignal.__str__()

        else:
            print("Signal ist nicht kontinuierlich")
            return None

# Kontinuierliche Signale
class sine(contiuous):
    def __init__(self, frequency = 1, amplitude = 1):
        self.frequency = float(frequency)
        self.amplitude = float(amplitude)
        self.type = "contiuous"

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
        self.type = "contiuous"

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
        self.type = "contiuous"

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
        self.type = "contiuous"

    def getYAt(self, x):
        return self.value

    def setValue(self, value):
        self._value = value

    def __str__(self):
        return str(self.value)


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

    def __str__(self):
        return self.sigA.__str__() + "+" + self.sigB.__str__()


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

    def __str__(self):
        return self.sigA.__str__() + "-" + self.sigB.__str__()


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

    def __str__(self):
        return self.sigA.__str__() + "*" + self.sigB.__str__()


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
