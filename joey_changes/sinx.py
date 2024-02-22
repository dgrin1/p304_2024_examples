import numpy as np
import math

x = float(input('x = '))%(2.e0*np.pi)
i = 0
s,sold = 0.e0,0.e0
while i<3000:
    sold= s
    s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
    i += 1
    if sold == s: 
    	print(i)
    	break
print(s)
    

