import numpy as np
import matplotlib.pyplot as plt
from . import signalgen as sig

class plot:
    def __init__(self, inputSig, samplingRate = 1, start = 0, end = 100):
        self.signal = inputSig
        self.samplingRate = samplingRate
        self.start = start
        self.end = end
        self.draw()

    def setSignal(self, inputSig):
        self.signal = inputSig
        self.plot()

    def draw(self):

        if self.signal.FisDiscrete:
            xValues = self.signal.getXList()
            yValues = self.signal.getYList()
            markerline, stemlines, baseline = plt.stem( xValues,yValues, '-.')
            plt.setp(markerline, linewidth=2, color='b')
            plt.setp(stemlines, linewidth=1, color='b')
            plt.setp(baseline, linewidth=2,color='black')
            plt.show()

        else:
            intv = 1 / self.samplingRate
            self.XVals = np.arange(self.start, self.end, intv)
            self.YVals = self.signal.getList(self.XVals)
            print(self.XVals)
            print(self.YVals)
            plt.plot(self.XVals, self.YVals)
            plt.xlabel("Zeit")
            plt.ylabel("Amplitude")
            plt.show()


class writeToFile:
    def __init__(self):
        pass
