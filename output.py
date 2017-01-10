from abc import ABCMeta, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
import signalgen

class diagram:
    def __init__(self, inputSig, samplRate = 1, start = 0, end = 100):
        self.signal = inputSig
        self.samplingRate = samplRate
        self.start = start
        self.end = end

    def setSignal(self, inputSig):
        self.signal = inputSig

    def plot(self):
        self.XVals = np.arange(self.start, self.end, 1 / self.samplingRate)
        self.YVals = self.signal.getList(self.XVals)
        print(self.XVals)
        print(self.YVals)
        plt.plot(self.XVals, self.YVals)
        # Input-Signale plotten
        pass

class writeToFile:
    def __init__(self):
        pass
