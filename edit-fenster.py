%matplotlib notebook
from ipywidgets import widgets
import signalgen
def f(y)
  print(y)
    if (y == ''):
      y = 10
    signalgen.sine(10, int(y))
widgets.interact(f, y = '10')
