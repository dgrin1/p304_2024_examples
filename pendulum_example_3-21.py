import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['backend']='TkAgg'
matplotlib.rcParams['text.usetex']='True'
matplotlib.rcParams['font.family']='serif'
matplotlib.rcParams['font.serif']='Times New Roman'
#plt.ion only works in interactive mode
plt.ion()

g = 9.81
# theta2 = np.arange(0, 6*np.pi, np.pi/4)

def theta(l, theta2):
    return np.arcsin(-theta2(l/g))

a = 0.0
b = 6*np.pi
N = 100000
h = (b-a)/N

thetapoints = np.arange(a,b,h)
lengthpoints = []
l = 0.0

for theta in thetapoints:
    lengthpoints.append(l)
    k1 = h*theta(l,theta)
    k2 = h*theta(l+0.5*k1,theta+0.5*h)
    k3 = h*theta(l+0.5*k2,theta+0.5*h)
    k4 = h*theta(l+k3,theta+h)
    l += (k1+2*k2+2*k3+k4)/6

plt.xlabel("theta2")
plt.ylabel("theta(theta2)")
plt.show()
