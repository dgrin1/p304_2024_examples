import numpy as np
from math import log, sin, cos, pi


#overkill in python 2 which can read in floats but necessary in python 3 which reads everything as a string initially
r=float(input("What is the radius?"))
th=float(input("What is the angle in degrees?"))
th_rad=th *pi/180.

x=r*cos(th_rad)
y=r*sin(th_rad)
print("Cartesian coordinates x=",x,"y=",y)