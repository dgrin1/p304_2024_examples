import numpy as np
import math

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
for y in range(2,101):
    r= trape(0,50,f(4),x[y])
    
    error.append(r)

#Call trapezoidal function to get integral estimate
#trape(a,b,f,N)
