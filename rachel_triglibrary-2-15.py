import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.rcParams['backend']='TkAgg'
matplotlib.rcParams['text.usetex']='True'
matplotlib.rcParams['font.family']='serif'
matplotlib.rcParams['font.serif']='Times New Roman'
#plt.ion only works in interactive mode
plt.ion()

x=np.arange(0, 2*np.pi, 100)
ySIN = np.sin(x)
yCOS = np.cos(x)
yTAN = np.tan(x)

plt.plot(x, ySIN)
plt.show()

plt.plot(x, yCOS)
plt.show()

plt.plot(x, yTAN)
plt.show()