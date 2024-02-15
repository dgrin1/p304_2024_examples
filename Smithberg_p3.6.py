#Feigenbaum plot

from numpy import append, array
from pylab import plot, show, xlabel, ylabel, scatter

def branch(r): #iterates the logistic map for one value of r
    x = 0.5
    xc = 0.e0  #x'
    i = 0
    for i in range(0,1000):
        xc = r*x*(1-x)
        x = xc
    rvals = []
    xvals = []
    for i in range(0,1000):
        xc = r*x*(1-x)
        xvals.append(xc)
        rvals.append(r)
        x = xc
    scatter(rvals,xvals)


branch(1)
show()
