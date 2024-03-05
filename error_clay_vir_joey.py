import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate

def f(x):
    return x**2

def trape(a,b,f,N):
#stepsize
        h=(b-a)/N
#End points
        s=(f(a)+f(b))*h
#Accumulate and normal sum by simpson formula
        for i in range(1,N):
                s+=2.*f(a+i*h)*h
        s/=2.0
        return s

error=[]
x=np.arange(1,101)
for y in range(1,101):
    r=abs((trape(0,50,f,x[y])-integrate.trapezoidal(f,x)/integrate.trapezoidal(f,x))
    error.append(r)
print(error)
