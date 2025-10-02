import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed, interact_manual
import ipywidgets as widget

def f(x):
  plt.plot(np.arange(0,10), x*np.arange(0,10))
  plt.ylim(-30,30)

# passando x = 0
#f(0)
interact(f, x=(-5, 10,1))
#plt.show()