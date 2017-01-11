from abc import ABCMeta, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import lib.signalgen

class diagram:
    def __init__(self, inputSig, samplingRate = 1, start = 0, end = 100):
        self.signal = inputSig
        self.samplingRate = samplingRate
        self.start = start
        self.end = end
        self.plot()

    def setSignal(self, inputSig):
        self.signal = inputSig
        self.plot()

    def plot(self):
        intv = 1 / self.samplingRate
        self.XVals = np.arange(self.start, self.end, intv)
        self.YVals = self.signal.getList(self.XVals)
        #print(self.XVals)
        #print(self.YVals)
        plt.plot(self.XVals, self.YVals)
        plt.xlabel("Zeit")
        plt.ylabel("Amplitude")
        plt.show()

class writeToFile:
    def __init__(self):
        pass
