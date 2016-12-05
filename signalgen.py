from abc import ABCMeta, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as wdgt

class signal(metaclass=ABCMeta):
    @abstractmethod
    def getYAt(self, x):
        pass

    def makeList(self, inList):
        outList = [self.getYAt(x) for x in inList]
        return outList

class sine(signal):
    def __init__(self, frequency = 1, amplitude = 1):
        self.frequency = frequency
        self.amplitude = amplitude

        self.fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        self.t = np.arange(0.0, 1.0, 0.001)
        self.s = self.makeList(self.t)
        self.l, = plt.plot(self.t, self.s, lw=1, color='red')

        plt.axis([0, 1, -10, 10])
        plt.grid()

        axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg='white')
        axamp = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg='white')

        self.sfreq = wdgt.Slider(axfreq, 'Freq', 0.1, 30.0, valinit=self.frequency)
        self.samp = wdgt.Slider(axamp, 'Amp', 0.1, 10.0, valinit=self.amplitude)

        self.sfreq.on_changed(self.update)
        self.samp.on_changed(self.update)

    def getYAt(self, time):
        return self.amplitude * np.sin(2 * np.pi * self.frequency * time)

    def setFreq(self, frequency):
        self.frequency = frequency

    def setAmp(self, amplitude):
        self.amplitude = amplitude

    def update(self):
        self.frequency = self.sfreq.val
        self.amplitude = self.samp.val
        self.s = self.makeList(self.t)
        self.l.set_ydata(self.s)
        self.fig.canvas.draw_idle()
        plt.show()

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


class const(signal):
    def __init__(self, value):
        self._value = value

    def getYAt(self, x):
        return self._value

    def setValue(self, value):
        self._value = value


class add(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) + self.sigB.getYAt(time)


class sub(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) - self.sigB.getYAt(time)


class mul(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) * self.sigB.getYAt(time)


class div(signal):
    def __init__(self, signalA, signalB):
        self.sigA = signalA
        self.sigB = signalB

    def getYAt(self, time):
        return self.sigA.getYAt(time) / self.sigB.getYAt(time)