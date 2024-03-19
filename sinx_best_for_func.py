import numpy as np
import math

def gsin(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s

<<<<<<< HEAD
a=float(input("What would you like to compute the sin of?"))
print(gsin(a))
=======
>>>>>>> 01f74b7743c1f73bea149a62cc4729e4435276ea
