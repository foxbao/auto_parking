import numpy as np
import matplotlib.pyplot as plt


class Visulizer:
  def __init__(self):
    self.aaa = 1
  
  def plot_map(self,map):
    dddd=2
  
  def plot_vehicle(self,vehicle):
    aaa=1
    
  

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()